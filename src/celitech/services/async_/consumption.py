from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..consumption import ConsumptionService
from ...net.sdk_config import SdkConfig


class ConsumptionServiceAsync(ConsumptionService):
    """
    Async Wrapper for ConsumptionServiceAsync
    """

    def get_purchase_consumption(
        self,
        purchase_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_purchase_consumption)(
            purchase_id, accept, request_config=request_config
        )
