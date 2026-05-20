from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..purchases import PurchasesService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL
from ...models import CreatePurchaseRequest


class PurchasesServiceAsync(PurchasesService):
    """
    Async Wrapper for PurchasesServiceAsync
    """

    def create_purchase(
        self,
        request_body: CreatePurchaseRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_purchase)(
            request_body, accept, request_config=request_config
        )

    def list_purchases(
        self,
        accept: Union[str, None],
        purchase_id: Union[str, None] = SENTINEL,
        iccid: Union[str, None] = SENTINEL,
        after_date: Union[str, None] = SENTINEL,
        before_date: Union[str, None] = SENTINEL,
        email: Union[str, None] = SENTINEL,
        reference_id: Union[str, None] = SENTINEL,
        after_cursor: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        after: Union[str, None] = SENTINEL,
        before: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().list_purchases)(
            accept,
            purchase_id,
            iccid,
            after_date,
            before_date,
            email,
            reference_id,
            after_cursor,
            limit,
            after,
            before,
            request_config=request_config,
        )
