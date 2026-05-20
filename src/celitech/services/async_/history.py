from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..history import HistoryService
from ...net.sdk_config import SdkConfig


class HistoryServiceAsync(HistoryService):
    """
    Async Wrapper for HistoryServiceAsync
    """

    def get_e_sim_history(
        self,
        iccid: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_e_sim_history)(
            iccid, accept, request_config=request_config
        )
