from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    BadRequest,
    GetEsimDeviceOkResponse,
    GetEsimHistoryOkResponse,
    GetEsimOkResponse,
    Unauthorized,
)


class ESimService(BaseService):
    """
    Service class for ESimService operations.
    Provides methods to interact with ESimService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._get_esim_config: SdkConfig = {}
        self._get_esim_device_config: SdkConfig = {}
        self._get_esim_history_config: SdkConfig = {}

    def set_get_esim_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_esim.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_esim_config = config
        return self

    def set_get_esim_device_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_esim_device.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_esim_device_config = config
        return self

    def set_get_esim_history_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_esim_history.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_esim_history_config = config
        return self

    @cast_models
    def get_esim(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> GetEsimOkResponse:
        """Get eSIM

        :param iccid: ID of the eSIM
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetEsimOkResponse
        """

        Validator(str).min_length(18).max_length(22).validate(iccid)

        resolved_config = self._get_resolved_config(
            self._get_esim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/esim",
                [],
                resolved_config,
            )
            .add_query("iccid", iccid)
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return GetEsimOkResponse.model_validate(response)

    @cast_models
    def get_esim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> GetEsimDeviceOkResponse:
        """Get eSIM Device

        :param iccid: ID of the eSIM
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetEsimDeviceOkResponse
        """

        Validator(str).min_length(18).max_length(22).validate(iccid)

        resolved_config = self._get_resolved_config(
            self._get_esim_device_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/esim/{{iccid}}/device",
                [],
                resolved_config,
            )
            .add_path("iccid", iccid)
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return GetEsimDeviceOkResponse.model_validate(response)

    @cast_models
    def get_esim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> GetEsimHistoryOkResponse:
        """Get eSIM History

        :param iccid: ID of the eSIM
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetEsimHistoryOkResponse
        """

        Validator(str).min_length(18).max_length(22).validate(iccid)

        resolved_config = self._get_resolved_config(
            self._get_esim_history_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/esim/{{iccid}}/history",
                [],
                resolved_config,
            )
            .add_path("iccid", iccid)
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return GetEsimHistoryOkResponse.model_validate(response)
