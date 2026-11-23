from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import ErrorResponse, ListPackagesResponse
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..core.request_options import RequestOptions
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
        self._raw_client = self.with_raw_response
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
        destination: Optional[str] = SENTINEL,
        data_limit_in_gb: Optional[float] = SENTINEL,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        start_time: Optional[int] = SENTINEL,
        end_time: Optional[int] = SENTINEL,
        include_unlimited: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListPackagesResponse:
        """
        List Packages

        Parameters
        ----------
        destination : typing.Optional[str]
            ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.

        data_limit_in_gb : typing.Optional[float]
            Filter packages by data limit in GB. When provided, only packages with this exact data limit are returned. Use `-1` together with `includeUnlimited=true` to return only unlimited packages. A value of `0` is ignored.

        start_date : typing.Optional[str]
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : typing.Optional[str]
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        after_cursor : typing.Optional[str]
            To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data.

        limit : typing.Optional[float]
            Maximum number of packages to be returned in the response. The value must be greater than 0 and less than or equal to 160. If not provided, the default value is 20

        start_time : typing.Optional[int]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months

        end_time : typing.Optional[int]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time

        include_unlimited : typing.Optional[bool]
            Whether to include unlimited (date-based) packages in the results. Unlimited packages are excluded by default; set this to `true` to include them. An unlimited package has `dataLimitInGB` and `dataLimitInBytes` equal to `-1`, and is offered for 3 to 30 days with `minDays` equal to `maxDays`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPackagesResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.packages.list_packages()
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
            self._list_packages_config, request_options
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
                else construct_lenient(ListPackagesResponse, response)
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
        self._client_wrapper = client._client_wrapper

    def list_packages(
        self,
        *,
        destination: Optional[str] = SENTINEL,
        data_limit_in_gb: Optional[float] = SENTINEL,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        start_time: Optional[int] = SENTINEL,
        end_time: Optional[int] = SENTINEL,
        include_unlimited: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPackagesResponse]:
        data = PackagesClient.list_packages(
            self._client,
            **dict[str, Any](
                {
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
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPackagesClient(PackagesClient):
    """
    Async wrapper for PackagesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawPackagesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPackagesClient(self)

    def list_packages(
        self,
        *,
        destination: Optional[str] = SENTINEL,
        data_limit_in_gb: Optional[float] = SENTINEL,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        start_time: Optional[int] = SENTINEL,
        end_time: Optional[int] = SENTINEL,
        include_unlimited: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListPackagesResponse]:  # type: ignore[override]
        """
        List Packages

        Parameters
        ----------
        destination : typing.Optional[str]
            ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.

        data_limit_in_gb : typing.Optional[float]
            Filter packages by data limit in GB. When provided, only packages with this exact data limit are returned. Use `-1` together with `includeUnlimited=true` to return only unlimited packages. A value of `0` is ignored.

        start_date : typing.Optional[str]
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : typing.Optional[str]
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        after_cursor : typing.Optional[str]
            To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data.

        limit : typing.Optional[float]
            Maximum number of packages to be returned in the response. The value must be greater than 0 and less than or equal to 160. If not provided, the default value is 20

        start_time : typing.Optional[int]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months

        end_time : typing.Optional[int]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time

        include_unlimited : typing.Optional[bool]
            Whether to include unlimited (date-based) packages in the results. Unlimited packages are excluded by default; set this to `true` to include them. An unlimited package has `dataLimitInGB` and `dataLimitInBytes` equal to `-1`, and is offered for 3 to 30 days with `minDays` equal to `maxDays`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPackagesResponse
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
            await client.packages.list_packages()


        asyncio.run(main())
        """
        return to_async(super().list_packages)(
            **dict[str, Any](
                {
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
                }
            ),
            request_options=request_options,
        )


class AsyncRawPackagesClient:
    """
    Async raw-response client for AsyncPackagesClient.
    """

    def __init__(self, client: AsyncPackagesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list_packages(
        self,
        *,
        destination: Optional[str] = SENTINEL,
        data_limit_in_gb: Optional[float] = SENTINEL,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        start_time: Optional[int] = SENTINEL,
        end_time: Optional[int] = SENTINEL,
        include_unlimited: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPackagesResponse]:
        data = await AsyncPackagesClient.list_packages(
            self._client,
            **dict[str, Any](
                {
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
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
