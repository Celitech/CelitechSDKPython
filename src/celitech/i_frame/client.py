from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import ErrorResponse, TokenResponse
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class IFrameClient(BaseService):
    """
    Fern-style resource client for IFrameClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._token_config: SdkConfig = {}

    def set_token_config(self, config: SdkConfig):
        """
        Sets method-level configuration for token.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._token_config = config
        return self

    @property
    def with_raw_response(self) -> "RawIFrameClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawIFrameClient(self)

    @cast_models
    def token(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Generate a new token to be used in the iFrame

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.i_frame.token()
        """

        resolved_config = self._get_resolved_config(self._token_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/iframe/token",
                [],
                resolved_config,
            )
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                TokenResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(TokenResponse, response)
            )
        )


class RawIFrameClient:
    """
    Raw-response client for IFrameClient.

    Each method delegates to the matching :class:`IFrameClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: IFrameClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def token(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[TokenResponse]:
        data = IFrameClient.token(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncIFrameClient(IFrameClient):
    """
    Async wrapper for IFrameClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawIFrameClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawIFrameClient(self)

    def token(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[TokenResponse]:  # type: ignore[override]
        """
        Generate a new token to be used in the iFrame

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Successful Response

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.i_frame.token()


        asyncio.run(main())
        """
        return to_async(super().token)(request_options=request_options)


class AsyncRawIFrameClient:
    """
    Async raw-response client for AsyncIFrameClient.
    """

    def __init__(self, client: AsyncIFrameClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def token(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[TokenResponse]:
        data = await AsyncIFrameClient.token(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
