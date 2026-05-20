from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..destinations import DestinationsService
from ...net.sdk_config import SdkConfig


class DestinationsServiceAsync(DestinationsService):
    """
    Async Wrapper for DestinationsServiceAsync
    """

    def list_destinations(
        self, accept: Union[str, None], *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().list_destinations)(
            accept, request_config=request_config
        )
