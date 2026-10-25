from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..models.utils.cast_models import cast_models
from ..models import ErrorResponse, ListDestinationsResponse
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class DestinationsClient(BaseService):
    """
    Fern-style resource client for DestinationsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._list_destinations_config: SdkConfig = {}

    def set_list_destinations_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_destinations.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_destinations_config = config
        return self

    @property
    def with_raw_response(self) -> "RawDestinationsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDestinationsClient(self)

    @cast_models
    def list_destinations(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> ListDestinationsResponse:
        """List Destinations

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListDestinationsResponse
        """

        resolved_config = self._get_resolved_config(
            self._list_destinations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/destinations",
                [],
                resolved_config,
            )
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListDestinationsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )


class RawDestinationsClient:
    """
    Raw-response client for DestinationsClient.

    Each method delegates to the matching :class:`DestinationsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DestinationsClient):
        self._client = client

    def list_destinations(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[ListDestinationsResponse]:
        data = self._client.list_destinations(request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDestinationsClient(DestinationsClient):
    """
    Async wrapper for DestinationsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawDestinationsClient":
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDestinationsClient(self)

    def list_destinations(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[ListDestinationsResponse]:
        return to_async(super().list_destinations)(request_config=request_config)


class AsyncRawDestinationsClient:
    """
    Async raw-response client for AsyncDestinationsClient.
    """

    def __init__(self, client: AsyncDestinationsClient):
        self._client = client

    async def list_destinations(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[ListDestinationsResponse]:
        data = await self._client.list_destinations(request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)
