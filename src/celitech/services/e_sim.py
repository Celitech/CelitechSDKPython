from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    ErrorResponse,
    GetEsimDeviceOkResponse,
    GetEsimHistoryOkResponse,
    GetEsimOkResponse,
    SuspendEsimOkResponse,
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
        self._suspend_esim_config: SdkConfig = {}

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

    def set_suspend_esim_config(self, config: SdkConfig):
        """
        Sets method-level configuration for suspend_esim.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._suspend_esim_config = config
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

        Validator(str).min_length(18).max_length(22).validate(iccid, "iccid")

        resolved_config = self._get_resolved_config(
            self._get_esim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.DEFAULT.url}/esim",
                [],
                resolved_config,
            )
            .add_query("iccid", iccid)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetEsimOkResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )

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

        Validator(str).min_length(18).max_length(22).validate(iccid, "iccid")

        resolved_config = self._get_resolved_config(
            self._get_esim_device_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.DEFAULT.url}/esim/{{iccid}}/device",
                [],
                resolved_config,
            )
            .add_path("iccid", iccid)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetEsimDeviceOkResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )

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

        Validator(str).min_length(18).max_length(22).validate(iccid, "iccid")

        resolved_config = self._get_resolved_config(
            self._get_esim_history_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.DEFAULT.url}/esim/{{iccid}}/history",
                [],
                resolved_config,
            )
            .add_path("iccid", iccid)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetEsimHistoryOkResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )

    @cast_models
    def suspend_esim(
        self,
        iccid: str,
        idempotency_key: str = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> SuspendEsimOkResponse:
        """Suspends an eSIM to prevent abuse. All of the eSIM's packages are terminated and its connectivity is switched off. The eSIM is not refunded: the charge stays.

        :param iccid: ID of the eSIM
        :type iccid: str
        :param idempotency_key: Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces., defaults to None
        :type idempotency_key: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: SuspendEsimOkResponse
        """

        Validator(str).min_length(18).max_length(22).validate(iccid, "iccid")
        Validator(str).is_optional().min_length(1).max_length(255).validate(
            idempotency_key, "idempotency_key"
        )

        resolved_config = self._get_resolved_config(
            self._suspend_esim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or Environment.DEFAULT.url}/esim/{{iccid}}/suspend",
                [],
                resolved_config,
            )
            .add_header("Idempotency-Key", idempotency_key)
            .add_path("iccid", iccid)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SuspendEsimOkResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )
