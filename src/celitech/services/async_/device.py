from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..device import DeviceService
from ...net.sdk_config import SdkConfig


class DeviceServiceAsync(DeviceService):
    """
    Async Wrapper for DeviceServiceAsync
    """

    def get_e_sim_device(
        self,
        iccid: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_e_sim_device)(
            iccid, accept, request_config=request_config
        )
