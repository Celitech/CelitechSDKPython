from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class ConsumptionService(BaseService):
    """
    Service class for ConsumptionService operations.
    Provides methods to interact with ConsumptionService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._get_purchase_consumption_config: SdkConfig = {
            "environment": Environment.API
        }

    def set_get_purchase_consumption_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_purchase_consumption.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_purchase_consumption_config = config
        return self

    @cast_models
    def get_purchase_consumption(
        self,
        purchase_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

        :param purchase_id: purchase_id
        :type purchase_id: str
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(purchase_id)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._get_purchase_consumption_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases/{{purchaseId}}/consumption",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_path("purchaseId", purchase_id)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
