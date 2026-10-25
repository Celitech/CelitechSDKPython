from typing import Any, Optional
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..models.utils.cast_models import cast_models
from ..models import (
    PostOauth2TokenRequest,
    PostOauth2TokenRequestGrantType,
    PostOauth2TokenResponse,
)
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
        grant_type: PostOauth2TokenRequestGrantType,
        client_id: str,
        client_secret: str,
        scope: str,
        request_config: Optional[SdkConfig] = None,
    ) -> PostOauth2TokenResponse:
        """get_access_token_

        :param request_body: The request body.
        :type request_body: PostOauth2TokenRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: PostOauth2TokenResponse
        """

        resolved_config = self._get_resolved_config(
            self._get_access_token__config, request_config
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
                else response
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

    def get_access_token_(
        self,
        *,
        grant_type: PostOauth2TokenRequestGrantType,
        client_id: str,
        client_secret: str,
        scope: str,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[PostOauth2TokenResponse]:
        data = self._client.get_access_token_(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncOAuthClient(OAuthClient):
    """
    Async wrapper for OAuthClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawOAuthClient":
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawOAuthClient(self)

    def get_access_token_(
        self,
        *,
        grant_type: PostOauth2TokenRequestGrantType,
        client_id: str,
        client_secret: str,
        scope: str,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[PostOauth2TokenResponse]:
        return to_async(super().get_access_token_)(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            request_config=request_config,
        )


class AsyncRawOAuthClient:
    """
    Async raw-response client for AsyncOAuthClient.
    """

    def __init__(self, client: AsyncOAuthClient):
        self._client = client

    async def get_access_token_(
        self,
        *,
        grant_type: PostOauth2TokenRequestGrantType,
        client_id: str,
        client_secret: str,
        scope: str,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[PostOauth2TokenResponse]:
        data = await self._client.get_access_token_(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)
