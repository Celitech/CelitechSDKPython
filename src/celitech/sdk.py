import warnings
from typing import Union
from .services.destinations import DestinationsService
from .services.packages import PackagesService
from .services.purchases import PurchasesService
from .services.e_sim import ESimService
from .services.i_frame import IFrameService
from .net.environment import Environment
from .net.oauth.token_manager import TokenManager


class Celitech:
    """
    Main SDK client class for Celitech.
    Provides centralized configuration and access to all service endpoints.
    Supports authentication, environment management, and global timeout settings.
    """

    def __init__(
        self,
        *,
        client_id: str = None,
        client_secret: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: float = None,
        timeout_ms: int = None,
        retry: "RetryConfig" = None,
        base_oauth_url: str = None,
    ):
        """
        Initializes Celitech the SDK class.
        """
        self.base_oauth_url = (
            base_oauth_url if base_oauth_url else "https://auth.celitech.net"
        )
        self._token_manager = TokenManager(base_oauth_url=self.base_oauth_url)

        _resolved_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self._base_url = _resolved_url.rstrip("/") if _resolved_url else _resolved_url
        self.destinations = DestinationsService(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.packages = PackagesService(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.purchases = PurchasesService(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.e_sim = ESimService(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.i_frame = IFrameService(
            base_url=self._base_url, token_manager=self._token_manager
        )
        self.set_client_id(client_id)
        self.set_client_secret(client_secret)
        if timeout_ms is not None:
            warnings.warn(
                "`timeout_ms` is deprecated; use `timeout` (in seconds) instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            timeout = timeout_ms / 1000 if timeout is None else timeout
        if timeout is None:
            timeout = 60
        self.set_timeout(timeout)
        if retry is not None:
            self.set_retry(retry)

    def set_base_url(self, base_url: Union[Environment, str]):
        """
        Sets the base URL for the entire SDK.

        :param Union[Environment, str] base_url: The base URL to be set.
        :return: The SDK instance.
        """
        _resolved_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self._base_url = _resolved_url.rstrip("/") if _resolved_url else _resolved_url

        self.destinations.set_base_url(self._base_url)
        self.packages.set_base_url(self._base_url)
        self.purchases.set_base_url(self._base_url)
        self.e_sim.set_base_url(self._base_url)
        self.i_frame.set_base_url(self._base_url)

        return self

    def set_base_oauth_url(self, base_oauth_url):
        """
        Sets the base oAuth URL for the entire SDK.
        """
        self.base_oauth_url = base_oauth_url
        self._token_manager.set_base_oauth_url(base_oauth_url)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for the entire SDK.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The SDK instance.
        """
        self.destinations.set_timeout(timeout)
        self.packages.set_timeout(timeout)
        self.purchases.set_timeout(timeout)
        self.e_sim.set_timeout(timeout)
        self.i_frame.set_timeout(timeout)

        return self

    def set_retry(self, retry: "RetryConfig"):
        """
        Sets the retry configuration for the entire SDK.

        :param RetryConfig retry: The retry configuration to be set.
        :return: The SDK instance.
        """
        self.destinations.set_retry(retry)
        self.packages.set_retry(retry)
        self.purchases.set_retry(retry)
        self.e_sim.set_retry(retry)
        self.i_frame.set_retry(retry)

        return self

    def set_client_id(self, client_id: str):
        """
        Sets the client_id for the entire SDK.

        :param str client_id: The client_id to be set.
        :return: The SDK instance.
        """
        self._token_manager.set_client_id(client_id)
        return self

    def set_client_secret(self, client_secret: str):
        """
        Sets the client_secret for the entire SDK.

        :param str client_secret: The client_secret to be set.
        :return: The SDK instance.
        """
        self._token_manager.set_client_secret(client_secret)
        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
