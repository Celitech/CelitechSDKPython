from typing import Any, Optional
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    PostOauth2TokenRequest,
    PostOauth2TokenRequestGrantType,
    PostOauth2TokenResponse,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class OAuthClient(BaseService):
    """
    Fern-style resource client for OAuthClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_access_token__config: SdkConfig = {}

    def set_get_access_token__config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_access_token_.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_access_token__config = config
        return self

    @property
    def with_raw_response(self) -> "RawOAuthClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawOAuthClient(self)

    @cast_models
    def get_access_token_(
        self,
        *,
        grant_type: PostOauth2TokenRequestGrantType = "client_credentials",
        client_id: str,
        client_secret: str,
        scope: str,
        request_options: Optional[RequestOptions] = None,
    ) -> PostOauth2TokenResponse:
        """
        get_access_token_

        Parameters
        ----------
        grant_type : PostOauth2TokenRequestGrantType

        client_id : str

        client_secret : str

        scope : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauth2TokenResponse
            OAuth token

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.o_auth.get_access_token_(
            grant_type="client_credentials",
            client_id="your_client_id",
            client_secret="your_client_secret",
            scope="read write",
        )
        """

        resolved_config = self._get_resolved_config(
            self._get_access_token__config, request_options
        )

        request_body = PostOauth2TokenRequest(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
        )
        Validator(PostOauth2TokenRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/oauth2/token",
                [],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "application/x-www-form-urlencoded")
        )

        response, _, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PostOauth2TokenResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PostOauth2TokenResponse, response)
            )
        )


class RawOAuthClient:
    """
    Raw-response client for OAuthClient.

    Each method delegates to the matching :class:`OAuthClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: OAuthClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get_access_token_(
        self,
        *,
        grant_type: PostOauth2TokenRequestGrantType = "client_credentials",
        client_id: str,
        client_secret: str,
        scope: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostOauth2TokenResponse]:
        data = OAuthClient.get_access_token_(
            self._client,
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncOAuthClient(OAuthClient):
    """
    Async wrapper for OAuthClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawOAuthClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawOAuthClient(self)

    def get_access_token_(
        self,
        *,
        grant_type: PostOauth2TokenRequestGrantType = "client_credentials",
        client_id: str,
        client_secret: str,
        scope: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PostOauth2TokenResponse]:  # type: ignore[override]
        """
        get_access_token_

        Parameters
        ----------
        grant_type : PostOauth2TokenRequestGrantType

        client_id : str

        client_secret : str

        scope : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauth2TokenResponse
            OAuth token

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.o_auth.get_access_token_(
                grant_type="client_credentials",
                client_id="your_client_id",
                client_secret="your_client_secret",
                scope="read write",
            )


        asyncio.run(main())
        """
        return to_async(super().get_access_token_)(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            request_options=request_options,
        )


class AsyncRawOAuthClient:
    """
    Async raw-response client for AsyncOAuthClient.
    """

    def __init__(self, client: AsyncOAuthClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get_access_token_(
        self,
        *,
        grant_type: PostOauth2TokenRequestGrantType = "client_credentials",
        client_id: str,
        client_secret: str,
        scope: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostOauth2TokenResponse]:
        data = await AsyncOAuthClient.get_access_token_(
            self._client,
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
