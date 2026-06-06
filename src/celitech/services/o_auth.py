from typing import Any, Optional
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import OAuthTokenRequest, OAuthTokenResponse


class OAuthService(BaseService):
    """
    Service class for OAuthService operations.
    Provides methods to interact with OAuthService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._get_access_token__config: SdkConfig = {}

    def set_get_access_token__config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_access_token_.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_access_token__config = config
        return self

    @cast_models
    def get_access_token_(
        self,
        request_body: OAuthTokenRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> OAuthTokenResponse:
        """get_access_token_

        :param request_body: The request body.
        :type request_body: OAuthTokenRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: OAuthTokenResponse
        """

        Validator(OAuthTokenRequest).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._get_access_token__config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/oauth2/token",
                [],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "application/x-www-form-urlencoded")
        )

        response, _, _ = self.send_request(serialized_request)
        return OAuthTokenResponse.model_validate(response)
