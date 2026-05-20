from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class TokenService(BaseService):
    """
    Service class for TokenService operations.
    Provides methods to interact with TokenService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._generate_token_config: SdkConfig = {"environment": Environment.API}

    def set_generate_token_config(self, config: SdkConfig):
        """
        Sets method-level configuration for generate_token.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._generate_token_config = config
        return self

    @cast_models
    def generate_token(
        self, accept: Union[str, None], *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """Generate a new token to be used in the iFrame

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
            self._generate_token_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/iframe/token",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
