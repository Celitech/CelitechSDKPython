from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..token import TokenService
from ...net.sdk_config import SdkConfig


class TokenServiceAsync(TokenService):
    """
    Async Wrapper for TokenServiceAsync
    """

    def generate_token(
        self, accept: Union[str, None], *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().generate_token)(accept, request_config=request_config)
