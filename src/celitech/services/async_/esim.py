from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..esim import EsimService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL


class EsimServiceAsync(EsimService):
    """
    Async Wrapper for EsimServiceAsync
    """

    def get_e_sim(
        self,
        accept: Union[str, None],
        iccid: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_e_sim)(accept, iccid, request_config=request_config)
