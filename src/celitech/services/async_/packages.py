from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..packages import PackagesService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL
from ...models import ListPackagesOkResponse


class PackagesServiceAsync(PackagesService):
    """
    Async Wrapper for PackagesServiceAsync
    """

    def list_packages(
        self,
        destination: str = SENTINEL,
        data_limit_in_gb: float = SENTINEL,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        start_time: int = SENTINEL,
        end_time: int = SENTINEL,
        include_unlimited: bool = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListPackagesOkResponse]:
        return to_async(super().list_packages)(
            **{
                k: v
                for k, v in {
                    "destination": destination,
                    "data_limit_in_gb": data_limit_in_gb,
                    "start_date": start_date,
                    "end_date": end_date,
                    "after_cursor": after_cursor,
                    "limit": limit,
                    "start_time": start_time,
                    "end_time": end_time,
                    "include_unlimited": include_unlimited,
                }.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
