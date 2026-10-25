from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..models.utils.cast_models import cast_models
from ..models import ErrorResponse, TokenResponse
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
    def token(self, *, request_config: Optional[SdkConfig] = None) -> TokenResponse:
        """Generate a new token to be used in the iFrame

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: TokenResponse
        """

        resolved_config = self._get_resolved_config(self._token_config, request_config)

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
                else response
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

    def token(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[TokenResponse]:
        data = self._client.token(request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncIFrameClient(IFrameClient):
    """
    Async wrapper for IFrameClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawIFrameClient":
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawIFrameClient(self)

    def token(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[TokenResponse]:
        return to_async(super().token)(request_config=request_config)


class AsyncRawIFrameClient:
    """
    Async raw-response client for AsyncIFrameClient.
    """

    def __init__(self, client: AsyncIFrameClient):
        self._client = client

    async def token(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[TokenResponse]:
        data = await self._client.token(request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)
