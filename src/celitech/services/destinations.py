from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class DestinationsService(BaseService):
    """
    Service class for DestinationsService operations.
    Provides methods to interact with DestinationsService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._list_destinations_config: SdkConfig = {"environment": Environment.API}

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
        self, accept: Union[str, None], *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """List Destinations

        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._list_destinations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/destinations",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
