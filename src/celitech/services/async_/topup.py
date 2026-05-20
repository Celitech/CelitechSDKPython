from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..topup import TopupService
from ...net.sdk_config import SdkConfig
from ...models import TopUpESimRequest


class TopupServiceAsync(TopupService):
    """
    Async Wrapper for TopupServiceAsync
    """

    def top_up_e_sim(
        self,
        request_body: TopUpESimRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().top_up_e_sim)(
            request_body, accept, request_config=request_config
        )
