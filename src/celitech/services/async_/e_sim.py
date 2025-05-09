from typing import Awaitable
from .utils.to_async import to_async
from ..e_sim import ESimService
from ...models import (
    GetEsimOkResponse,
    GetEsimDeviceOkResponse,
    GetEsimHistoryOkResponse,
    GetEsimMacOkResponse,
)


class ESimServiceAsync(ESimService):
    """
    Async Wrapper for ESimServiceAsync
    """

    def get_esim(self, iccid: str) -> Awaitable[GetEsimOkResponse]:
        return to_async(super().get_esim)(iccid)

    def get_esim_device(self, iccid: str) -> Awaitable[GetEsimDeviceOkResponse]:
        return to_async(super().get_esim_device)(iccid)

    def get_esim_history(self, iccid: str) -> Awaitable[GetEsimHistoryOkResponse]:
        return to_async(super().get_esim_history)(iccid)

    def get_esim_mac(self, iccid: str) -> Awaitable[GetEsimMacOkResponse]:
        return to_async(super().get_esim_mac)(iccid)
