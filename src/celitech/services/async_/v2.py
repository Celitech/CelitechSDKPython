from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..v2 import V2Service
from ...net.sdk_config import SdkConfig
from ...models import CreatePurchaseV2Request


class V2ServiceAsync(V2Service):
    """
    Async Wrapper for V2ServiceAsync
    """

    def create_purchase_v2(
        self,
        request_body: CreatePurchaseV2Request,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_purchase_v2)(
            request_body, accept, request_config=request_config
        )
