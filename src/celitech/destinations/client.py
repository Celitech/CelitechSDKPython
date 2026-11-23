from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import ErrorResponse, ListDestinationsResponse
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..core.request_options import RequestOptions
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
        self._raw_client = self.with_raw_response
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
        self, *, request_options: Optional[RequestOptions] = None
    ) -> ListDestinationsResponse:
        """
        List Destinations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDestinationsResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.destinations.list_destinations()
        """

        resolved_config = self._get_resolved_config(
            self._list_destinations_config, request_options
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
                else construct_lenient(ListDestinationsResponse, response)
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
        self._client_wrapper = client._client_wrapper

    def list_destinations(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ListDestinationsResponse]:
        data = DestinationsClient.list_destinations(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDestinationsClient(DestinationsClient):
    """
    Async wrapper for DestinationsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawDestinationsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDestinationsClient(self)

    def list_destinations(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[ListDestinationsResponse]:  # type: ignore[override]
        """
        List Destinations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDestinationsResponse
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
            await client.destinations.list_destinations()


        asyncio.run(main())
        """
        return to_async(super().list_destinations)(request_options=request_options)


class AsyncRawDestinationsClient:
    """
    Async raw-response client for AsyncDestinationsClient.
    """

    def __init__(self, client: AsyncDestinationsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list_destinations(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ListDestinationsResponse]:
        data = await AsyncDestinationsClient.list_destinations(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
