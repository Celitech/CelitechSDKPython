from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import BadRequest, ListDestinationsOkResponse, Unauthorized


class DestinationsService(BaseService):
    """
    Service class for DestinationsService operations.
    Provides methods to interact with DestinationsService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
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

    @cast_models
    def list_destinations(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> ListDestinationsOkResponse:
        """List Destinations

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListDestinationsOkResponse
        """

        resolved_config = self._get_resolved_config(
            self._list_destinations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/destinations",
                [],
                resolved_config,
            )
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return ListDestinationsOkResponse.model_validate(response)
