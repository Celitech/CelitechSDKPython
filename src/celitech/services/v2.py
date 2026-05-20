from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import CreatePurchaseV2Request


class V2Service(BaseService):
    """
    Service class for V2Service operations.
    Provides methods to interact with V2Service-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._create_purchase_v2_config: SdkConfig = {"environment": Environment.API}

    def set_create_purchase_v2_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_purchase_v2.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_purchase_v2_config = config
        return self

    @cast_models
    def create_purchase_v2(
        self,
        request_body: CreatePurchaseV2Request,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseV2Request
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreatePurchaseV2Request).is_nullable().validate(request_body)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._create_purchase_v2_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases/v2",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response
