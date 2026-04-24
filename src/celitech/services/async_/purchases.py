from typing import Awaitable, Optional, List, Union
from .utils.to_async import to_async
from ..purchases import PurchasesService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL
from ...models import (
    CreatePurchaseV2OkResponse,
    CreatePurchaseV2Request,
    ListPurchasesOkResponse,
    CreatePurchaseOkResponse,
    CreatePurchaseRequest,
    TopUpEsimOkResponse,
    TopUpEsimRequest,
    EditPurchaseOkResponse,
    EditPurchaseRequest,
    GetPurchaseConsumptionOkResponse,
)


class PurchasesServiceAsync(PurchasesService):
    """
    Async Wrapper for PurchasesServiceAsync
    """

    def create_purchase_v2(
        self,
        request_body: CreatePurchaseV2Request,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[List[CreatePurchaseV2OkResponse]]:
        return to_async(super().create_purchase_v2)(
            request_body, request_config=request_config
        )

    def list_purchases(
        self,
        purchase_id: str = SENTINEL,
        iccid: str = SENTINEL,
        after_date: str = SENTINEL,
        before_date: str = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        after: float = SENTINEL,
        before: float = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListPurchasesOkResponse]:
        return to_async(super().list_purchases)(
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

    def create_purchase(
        self,
        request_body: CreatePurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[CreatePurchaseOkResponse]:
        return to_async(super().create_purchase)(
            request_body, request_config=request_config
        )

    def top_up_esim(
        self,
        request_body: TopUpEsimRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[TopUpEsimOkResponse]:
        return to_async(super().top_up_esim)(
            request_body, request_config=request_config
        )

    def edit_purchase(
        self,
        request_body: EditPurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[EditPurchaseOkResponse]:
        return to_async(super().edit_purchase)(
            request_body, request_config=request_config
        )

    def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetPurchaseConsumptionOkResponse]:
        return to_async(super().get_purchase_consumption)(
            purchase_id, request_config=request_config
        )
