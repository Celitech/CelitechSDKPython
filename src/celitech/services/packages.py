from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import BadRequest, ListPackagesOkResponse, Unauthorized


class PackagesService(BaseService):
    """
    Service class for PackagesService operations.
    Provides methods to interact with PackagesService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
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

    @cast_models
    def list_packages(
        self,
        destination: str = SENTINEL,
        data_limit_in_gb: float = SENTINEL,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        start_time: int = SENTINEL,
        end_time: int = SENTINEL,
        include_unlimited: bool = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> ListPackagesOkResponse:
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
        :rtype: ListPackagesOkResponse
        """

        Validator(str).is_optional().validate(destination)
        Validator(float).is_optional().validate(data_limit_in_gb)
        Validator(str).is_optional().validate(start_date)
        Validator(str).is_optional().validate(end_date)
        Validator(str).is_optional().validate(after_cursor)
        Validator(float).is_optional().validate(limit)
        Validator(int).is_optional().validate(start_time)
        Validator(int).is_optional().validate(end_time)
        Validator(bool).is_optional().validate(include_unlimited)

        resolved_config = self._get_resolved_config(
            self._list_packages_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/packages",
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
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else ListPackagesOkResponse.model_validate(response)
        )
