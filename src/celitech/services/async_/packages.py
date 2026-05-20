from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..packages import PackagesService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL


class PackagesServiceAsync(PackagesService):
    """
    Async Wrapper for PackagesServiceAsync
    """

    def list_packages(
        self,
        accept: Union[str, None],
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
            accept,
            destination,
            start_date,
            end_date,
            after_cursor,
            limit,
            start_time,
            end_time,
            request_config=request_config,
        )
