from typing import Union
from .net.environment import Environment
from .sdk import Celitech
from .services.async_.destinations import DestinationsServiceAsync
from .services.async_.packages import PackagesServiceAsync
from .services.async_.v2 import V2ServiceAsync
from .services.async_.topup import TopupServiceAsync
from .services.async_.edit import EditServiceAsync
from .services.async_.consumption import ConsumptionServiceAsync
from .services.async_.purchases import PurchasesServiceAsync
from .services.async_.device import DeviceServiceAsync
from .services.async_.history import HistoryServiceAsync
from .services.async_.esim import EsimServiceAsync
from .services.async_.token import TokenServiceAsync
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

        self.destinations = DestinationsServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.packages = PackagesServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.v2 = V2ServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.topup = TopupServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.edit = EditServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.consumption = ConsumptionServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.purchases = PurchasesServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.device = DeviceServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.history = HistoryServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.esim = EsimServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.token = TokenServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.o_auth = OAuthServiceAsync(
            base_url=self._base_url, token_manager=self._token_manager
        )
