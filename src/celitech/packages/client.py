from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import ErrorResponse, ListPackagesResponse
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class PackagesClient(BaseService):
    """
    Fern-style resource client for PackagesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._list_packages_config: SdkConfig = {}

    def set_list_packages_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_packages.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_packages_config = config
        return self

    @property
    def with_raw_response(self) -> "RawPackagesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawPackagesClient(self)

    @cast_models
    def list_packages(
        self,
        *,
        destination: str = SENTINEL,
        data_limit_in_gb: float = SENTINEL,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        start_time: int = SENTINEL,
        end_time: int = SENTINEL,
        include_unlimited: bool = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> ListPackagesResponse:
        """List Packages

        :param destination: ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes., defaults to None
        :type destination: str, optional
        :param data_limit_in_gb: Filter packages by data limit in GB. When provided, only packages with this exact data limit are returned. Use `-1` together with `includeUnlimited=true` to return only unlimited packages. A value of `0` is ignored., defaults to None
        :type data_limit_in_gb: float, optional
        :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months., defaults to None
        :type start_date: str, optional
        :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date., defaults to None
        :type end_date: str, optional
        :param after_cursor: To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data., defaults to None
        :type after_cursor: str, optional
        :param limit: Maximum number of packages to be returned in the response. The value must be greater than 0 and less than or equal to 160. If not provided, the default value is 20, defaults to None
        :type limit: float, optional
        :param start_time: Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months, defaults to None
        :type start_time: int, optional
        :param end_time: Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time, defaults to None
        :type end_time: int, optional
        :param include_unlimited: Whether to include unlimited (date-based) packages in the results. Unlimited packages are excluded by default; set this to `true` to include them. An unlimited package has `dataLimitInGB` and `dataLimitInBytes` equal to `-1`, and is offered for 3 to 30 days with `minDays` equal to `maxDays`., defaults to None
        :type include_unlimited: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListPackagesResponse
        """

        Validator(str).is_optional().validate(destination, "destination")
        Validator(float).is_optional().validate(data_limit_in_gb, "data_limit_in_gb")
        Validator(str).is_optional().validate(start_date, "start_date")
        Validator(str).is_optional().validate(end_date, "end_date")
        Validator(str).is_optional().validate(after_cursor, "after_cursor")
        Validator(float).is_optional().validate(limit, "limit")
        Validator(int).is_optional().validate(start_time, "start_time")
        Validator(int).is_optional().validate(end_time, "end_time")
        Validator(bool).is_optional().validate(include_unlimited, "include_unlimited")

        resolved_config = self._get_resolved_config(
            self._list_packages_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/packages",
                [],
                resolved_config,
            )
            .add_query("destination", destination)
            .add_query("dataLimitInGB", data_limit_in_gb)
            .add_query("startDate", start_date)
            .add_query("endDate", end_date)
            .add_query("afterCursor", after_cursor)
            .add_query("limit", limit)
            .add_query("startTime", start_time)
            .add_query("endTime", end_time)
            .add_query("includeUnlimited", include_unlimited)
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
                ListPackagesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )


class RawPackagesClient:
    """
    Raw-response client for PackagesClient.

    Each method delegates to the matching :class:`PackagesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: PackagesClient):
        self._client = client

    def list_packages(
        self,
        *,
        destination: str = SENTINEL,
        data_limit_in_gb: float = SENTINEL,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        start_time: int = SENTINEL,
        end_time: int = SENTINEL,
        include_unlimited: bool = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[ListPackagesResponse]:
        data = self._client.list_packages(
            **{
                k: v
                for k, v in {
                    "destination": destination,
                    "data_limit_in_gb": data_limit_in_gb,
                    "start_date": start_date,
                    "end_date": end_date,
                    "after_cursor": after_cursor,
                    "limit": limit,
                    "start_time": start_time,
                    "end_time": end_time,
                    "include_unlimited": include_unlimited,
                }.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPackagesClient(PackagesClient):
    """
    Async wrapper for PackagesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawPackagesClient":
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPackagesClient(self)

    def list_packages(
        self,
        *,
        destination: str = SENTINEL,
        data_limit_in_gb: float = SENTINEL,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        start_time: int = SENTINEL,
        end_time: int = SENTINEL,
        include_unlimited: bool = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListPackagesResponse]:
        return to_async(super().list_packages)(
            **{
                k: v
                for k, v in {
                    "destination": destination,
                    "data_limit_in_gb": data_limit_in_gb,
                    "start_date": start_date,
                    "end_date": end_date,
                    "after_cursor": after_cursor,
                    "limit": limit,
                    "start_time": start_time,
                    "end_time": end_time,
                    "include_unlimited": include_unlimited,
                }.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )


class AsyncRawPackagesClient:
    """
    Async raw-response client for AsyncPackagesClient.
    """

    def __init__(self, client: AsyncPackagesClient):
        self._client = client

    async def list_packages(
        self,
        *,
        destination: str = SENTINEL,
        data_limit_in_gb: float = SENTINEL,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        start_time: int = SENTINEL,
        end_time: int = SENTINEL,
        include_unlimited: bool = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[ListPackagesResponse]:
        data = await self._client.list_packages(
            **{
                k: v
                for k, v in {
                    "destination": destination,
                    "data_limit_in_gb": data_limit_in_gb,
                    "start_date": start_date,
                    "end_date": end_date,
                    "after_cursor": after_cursor,
                    "limit": limit,
                    "start_time": start_time,
                    "end_time": end_time,
                    "include_unlimited": include_unlimited,
                }.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)
