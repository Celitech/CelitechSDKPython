from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    ErrorResponse,
    GetEsimDeviceResponse,
    GetEsimHistoryResponse,
    GetEsimResponse,
    SuspendEsimResponse,
)
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class ESimClient(BaseService):
    """
    Fern-style resource client for ESimClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
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

    @property
    def with_raw_response(self) -> "RawESimClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawESimClient(self)

    @cast_models
    def get_esim(
        self, *, iccid: str, request_config: Optional[SdkConfig] = None
    ) -> GetEsimResponse:
        """Get eSIM

        :param iccid: ID of the eSIM
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetEsimResponse
        """

        Validator(str).validate(iccid, "iccid")

        resolved_config = self._get_resolved_config(
            self._get_esim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/esim",
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
                GetEsimResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )

    @cast_models
    def get_esim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> GetEsimDeviceResponse:
        """Get eSIM Device

        :param iccid: ID of the eSIM
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetEsimDeviceResponse
        """

        Validator(str).validate(iccid, "iccid")

        resolved_config = self._get_resolved_config(
            self._get_esim_device_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/esim/{{iccid}}/device",
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
                GetEsimDeviceResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )

    @cast_models
    def get_esim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> GetEsimHistoryResponse:
        """Get eSIM History

        :param iccid: ID of the eSIM
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetEsimHistoryResponse
        """

        Validator(str).validate(iccid, "iccid")

        resolved_config = self._get_resolved_config(
            self._get_esim_history_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/esim/{{iccid}}/history",
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
                GetEsimHistoryResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )

    @cast_models
    def suspend_esim(
        self,
        iccid: str,
        *,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> SuspendEsimResponse:
        """Suspends an eSIM to prevent abuse. All of the eSIM's packages are terminated and its connectivity is switched off. The eSIM is not refunded: the charge stays.

        :param iccid: ID of the eSIM
        :type iccid: str
        :param idempotency_key: Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces., defaults to None
        :type idempotency_key: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: SuspendEsimResponse
        """

        Validator(str).validate(iccid, "iccid")
        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._suspend_esim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/esim/{{iccid}}/suspend",
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
                SuspendEsimResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else response
            )
        )


class RawESimClient:
    """
    Raw-response client for ESimClient.

    Each method delegates to the matching :class:`ESimClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ESimClient):
        self._client = client

    def get_esim(
        self, *, iccid: str, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetEsimResponse]:
        data = self._client.get_esim(iccid=iccid, request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)

    def get_esim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetEsimDeviceResponse]:
        data = self._client.get_esim_device(iccid, request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)

    def get_esim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetEsimHistoryResponse]:
        data = self._client.get_esim_history(iccid, request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)

    def suspend_esim(
        self,
        iccid: str,
        *,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[SuspendEsimResponse]:
        data = self._client.suspend_esim(
            iccid,
            **{
                k: v
                for k, v in {"idempotency_key": idempotency_key}.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncESimClient(ESimClient):
    """
    Async wrapper for ESimClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawESimClient":
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawESimClient(self)

    def get_esim(
        self, *, iccid: str, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetEsimResponse]:
        return to_async(super().get_esim)(iccid=iccid, request_config=request_config)

    def get_esim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetEsimDeviceResponse]:
        return to_async(super().get_esim_device)(iccid, request_config=request_config)

    def get_esim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetEsimHistoryResponse]:
        return to_async(super().get_esim_history)(iccid, request_config=request_config)

    def suspend_esim(
        self,
        iccid: str,
        *,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[SuspendEsimResponse]:
        return to_async(super().suspend_esim)(
            iccid,
            **{
                k: v
                for k, v in {"idempotency_key": idempotency_key}.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )


class AsyncRawESimClient:
    """
    Async raw-response client for AsyncESimClient.
    """

    def __init__(self, client: AsyncESimClient):
        self._client = client

    async def get_esim(
        self, *, iccid: str, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetEsimResponse]:
        data = await self._client.get_esim(iccid=iccid, request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_esim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetEsimDeviceResponse]:
        data = await self._client.get_esim_device(iccid, request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_esim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetEsimHistoryResponse]:
        data = await self._client.get_esim_history(iccid, request_config=request_config)
        return HttpResponse(data=data, response=self._client._last_response)

    async def suspend_esim(
        self,
        iccid: str,
        *,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[SuspendEsimResponse]:
        data = await self._client.suspend_esim(
            iccid,
            **{
                k: v
                for k, v in {"idempotency_key": idempotency_key}.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)
