from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..e_sim import ESimService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL
from ...models import (
    GetEsimOkResponse,
    GetEsimDeviceOkResponse,
    GetEsimHistoryOkResponse,
    SuspendEsimOkResponse,
)


class ESimServiceAsync(ESimService):
    """
    Async Wrapper for ESimServiceAsync
    """

    def get_esim(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetEsimOkResponse]:
        return to_async(super().get_esim)(iccid, request_config=request_config)

    def get_esim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetEsimDeviceOkResponse]:
        return to_async(super().get_esim_device)(iccid, request_config=request_config)

    def get_esim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetEsimHistoryOkResponse]:
        return to_async(super().get_esim_history)(iccid, request_config=request_config)

    def suspend_esim(
        self,
        iccid: str,
        idempotency_key: str = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[SuspendEsimOkResponse]:
        return to_async(super().suspend_esim)(
            iccid,
            **{
                k: v
                for k, v in {"idempotency_key": idempotency_key}.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
