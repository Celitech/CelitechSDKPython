from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models


class EsimService(BaseService):
    """
    Service class for EsimService operations.
    Provides methods to interact with EsimService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._get_e_sim_config: SdkConfig = {"environment": Environment.API}

    def set_get_e_sim_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_e_sim.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_e_sim_config = config
        return self

    @cast_models
    def get_e_sim(
        self,
        accept: Union[str, None],
        iccid: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Get eSIM

        :param accept: accept
        :type accept: str
        :param iccid: ID of the eSIM, defaults to None
        :type iccid: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).is_nullable().validate(accept)
        Validator(str).is_optional().is_nullable().validate(iccid)

        resolved_config = self._get_resolved_config(
            self._get_e_sim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/esim",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_query("iccid", iccid, nullable=True)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
