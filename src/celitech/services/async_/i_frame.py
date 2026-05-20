from typing import Awaitable, Optional, Union
from .utils.to_async import to_async
from ..i_frame import IFrameService
from ...net.sdk_config import SdkConfig
from ...models import TokenOkResponse


class IFrameServiceAsync(IFrameService):
    """
    Async Wrapper for IFrameServiceAsync
    """

    def token(
        self, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[TokenOkResponse]:
        return to_async(super().token)(request_config=request_config)
