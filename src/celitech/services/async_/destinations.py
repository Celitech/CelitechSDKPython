from typing import Awaitable, Optional, Union
from .utils.to_async import to_async
from ..destinations import DestinationsService
from ...net.sdk_config import SdkConfig
from ...models import ListDestinationsOkResponse


class DestinationsServiceAsync(DestinationsService):
    """
    Async Wrapper for DestinationsServiceAsync
    """

    def list_destinations(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[ListDestinationsOkResponse]:
        return to_async(super().list_destinations)(request_config=request_config)
