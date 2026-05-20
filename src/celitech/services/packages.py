from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models


class PackagesService(BaseService):
    """
    Service class for PackagesService operations.
    Provides methods to interact with PackagesService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._list_packages_config: SdkConfig = {"environment": Environment.API}

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
        accept: Union[str, None],
        destination: Union[str, None] = SENTINEL,
        start_date: Union[str, None] = SENTINEL,
        end_date: Union[str, None] = SENTINEL,
        after_cursor: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        start_time: Union[str, None] = SENTINEL,
        end_time: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """List Packages

        :param accept: accept
        :type accept: str
        :param destination: ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes., defaults to None
        :type destination: str, optional
        :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months., defaults to None
        :type start_date: str, optional
        :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date., defaults to None
        :type end_date: str, optional
        :param after_cursor: To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data., defaults to None
        :type after_cursor: str, optional
        :param limit: Maximum number of packages to be returned in the response. The value must be greater than 0 and less than or equal to 160. If not provided, the default value is 20, defaults to None
        :type limit: str, optional
        :param start_time: Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months, defaults to None
        :type start_time: str, optional
        :param end_time: Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time, defaults to None
        :type end_time: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).is_nullable().validate(accept)
        Validator(str).is_optional().is_nullable().validate(destination)
        Validator(str).is_optional().is_nullable().validate(start_date)
        Validator(str).is_optional().is_nullable().validate(end_date)
        Validator(str).is_optional().is_nullable().validate(after_cursor)
        Validator(str).is_optional().is_nullable().validate(limit)
        Validator(str).is_optional().is_nullable().validate(start_time)
        Validator(str).is_optional().is_nullable().validate(end_time)

        resolved_config = self._get_resolved_config(
            self._list_packages_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/packages",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_query("destination", destination, nullable=True)
            .add_query("startDate", start_date, nullable=True)
            .add_query("endDate", end_date, nullable=True)
            .add_query("afterCursor", after_cursor, nullable=True)
            .add_query("limit", limit, nullable=True)
            .add_query("startTime", start_time, nullable=True)
            .add_query("endTime", end_time, nullable=True)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
