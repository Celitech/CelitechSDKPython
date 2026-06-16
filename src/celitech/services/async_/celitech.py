from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..celitech import CelitechService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL
from ...models import (
    CreatePurchaseV2Request,
    TopUpESimRequest,
    EditPurchaseRequest,
    CreatePurchaseRequest,
)


class CelitechServiceAsync(CelitechService):
    """
    Async Wrapper for CelitechServiceAsync
    """

    def list_destinations(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().list_destinations)(request_config=request_config)

    def list_packages(
        self,
        destination: Union[str, None] = SENTINEL,
        start_date: Union[str, None] = SENTINEL,
        end_date: Union[str, None] = SENTINEL,
        after_cursor: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        start_time: Union[str, None] = SENTINEL,
        end_time: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().list_packages)(
            destination,
            start_date,
            end_date,
            after_cursor,
            limit,
            start_time,
            end_time,
            request_config=request_config,
        )

    def create_purchase_v2(
        self,
        request_body: CreatePurchaseV2Request,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_purchase_v2)(
            request_body, request_config=request_config
        )

    def top_up_e_sim(
        self,
        request_body: TopUpESimRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().top_up_e_sim)(
            request_body, request_config=request_config
        )

    def edit_purchase(
        self,
        request_body: EditPurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().edit_purchase)(
            request_body, request_config=request_config
        )

    def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().get_purchase_consumption)(
            purchase_id, request_config=request_config
        )

    def create_purchase(
        self,
        request_body: CreatePurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_purchase)(
            request_body, request_config=request_config
        )

    def list_purchases(
        self,
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

    def get_e_sim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().get_e_sim_device)(iccid, request_config=request_config)

    def get_e_sim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().get_e_sim_history)(iccid, request_config=request_config)

    def get_e_sim(
        self,
        iccid: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_e_sim)(iccid, request_config=request_config)

    def generate_token(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().generate_token)(request_config=request_config)
