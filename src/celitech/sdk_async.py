from typing import Union
from .net.environment import Environment
from .sdk import Celitech
from .services.async_.celitech import CelitechServiceAsync
from .services.async_.o_auth import OAuthServiceAsync


class CelitechAsync(Celitech):
    """
    CelitechAsync is the asynchronous version of the Celitech SDK Client.
    """

    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
        base_oauth_url: str = None,
    ):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            base_url=base_url,
            timeout=timeout,
            base_oauth_url=base_oauth_url,
        )

        self.celitech = CelitechServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.o_auth = OAuthServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
