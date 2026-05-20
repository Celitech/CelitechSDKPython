from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..edit import EditService
from ...net.sdk_config import SdkConfig
from ...models import EditPurchaseRequest


class EditServiceAsync(EditService):
    """
    Async Wrapper for EditServiceAsync
    """

    def edit_purchase(
        self,
        request_body: EditPurchaseRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().edit_purchase)(
            request_body, accept, request_config=request_config
        )
