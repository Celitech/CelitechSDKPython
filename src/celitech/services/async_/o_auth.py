from typing import Awaitable, Optional
from .utils.to_async import to_async
from ..o_auth import OAuthService
from ...net.sdk_config import SdkConfig
from ...models import OAuthTokenResponse, OAuthTokenRequest


class OAuthServiceAsync(OAuthService):
    """
    Async Wrapper for OAuthServiceAsync
    """

    def get_access_token_(
        self,
        request_body: OAuthTokenRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[OAuthTokenResponse]:
        return to_async(super().get_access_token_)(
            request_body, request_config=request_config
        )
