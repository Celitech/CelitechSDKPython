from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class HistoryService(BaseService):
    """
    Service class for HistoryService operations.
    Provides methods to interact with HistoryService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._get_e_sim_history_config: SdkConfig = {"environment": Environment.API}

    def set_get_e_sim_history_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_e_sim_history.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_e_sim_history_config = config
        return self

    @cast_models
    def get_e_sim_history(
        self,
        iccid: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Get eSIM History

        :param iccid: iccid
        :type iccid: str
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(iccid)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._get_e_sim_history_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/esim/{{iccid}}/history",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_path("iccid", iccid)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
