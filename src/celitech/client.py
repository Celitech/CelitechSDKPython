import warnings
import requests
import logging
from typing import Optional, TYPE_CHECKING, Union
from .net.environment import CelitechEnvironment
from .services.utils.base_service import BaseService
from .net.sdk_config import SdkConfig
from .net.oauth.token_manager import TokenManager

if TYPE_CHECKING:
    from .destinations.client import DestinationsClient, AsyncDestinationsClient
    from .packages.client import PackagesClient, AsyncPackagesClient
    from .purchases.client import PurchasesClient, AsyncPurchasesClient
    from .e_sim.client import ESimClient, AsyncESimClient
    from .i_frame.client import IFrameClient, AsyncIFrameClient
    from .o_auth.client import OAuthClient, AsyncOAuthClient


class Celitech(BaseService):
    """
    Main SDK client for Celitech (Fern nested resource layout).
    Exposes each top-level resource as a lazy accessor (`client.<resource>.method(...)`),
    threads a single configured transport down to every nested resource client, and binds
    any ungrouped (root) endpoints directly.
    """

    def __init__(
        self,
        *,
        client_id: str = None,
        client_secret: str = None,
        base_url: Union[CelitechEnvironment, str, None] = None,
        environment: Optional[CelitechEnvironment] = None,
        timeout: float = None,
        timeout_ms: int = None,
        http_client: Optional[requests.Session] = None,
        follow_redirects: bool = True,
        logger: Optional[logging.Logger] = None,
        retry: "RetryConfig" = None,
        stream_reconnection_enabled: Optional[bool] = None,
        max_stream_reconnection_attempts: Optional[int] = None,
        base_oauth_url: str = None,
    ):
        """Initializes the Celitech SDK client."""
        self.base_oauth_url = (
            base_oauth_url if base_oauth_url else "https://auth.celitech.net"
        )
        self._token_manager = TokenManager(
            base_oauth_url=self.base_oauth_url,
            http_client=http_client,
            follow_redirects=follow_redirects,
            logger=logger,
        )
        if environment is not None and base_url is None:
            base_url = environment
        _resolved_url = (
            base_url.value if isinstance(base_url, CelitechEnvironment) else base_url
        )
        super().__init__(
            base_url=_resolved_url,
            http_client=http_client,
            follow_redirects=follow_redirects,
            logger=logger,
            token_manager=self._token_manager,
        )
        self._destinations = None
        self._packages = None
        self._purchases = None
        self._e_sim = None
        self._i_frame = None
        self._o_auth = None
        self._token_manager.set_client_id(client_id)
        self._token_manager.set_client_secret(client_secret)
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
        if stream_reconnection_enabled is not None:
            self.set_config(
                {
                    **self._service_config,
                    "stream_reconnection_enabled": stream_reconnection_enabled,
                }
            )
        if max_stream_reconnection_attempts is not None:
            self.set_config(
                {
                    **self._service_config,
                    "max_stream_reconnection_attempts": max_stream_reconnection_attempts,
                }
            )

    def set_base_url(self, base_url: Union[CelitechEnvironment, str]):
        """
        Sets the base URL for the whole SDK, including every resource client already built.

        Resource clients are built lazily and cached holding a COPY of the root's base URL, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error. Each
        child forwards to its own sub-resources in turn.

        :param base_url: The base URL to be set, as a string or an CelitechEnvironment enum member.
        :return: The SDK instance.
        """
        super().set_base_url(base_url)
        if self._destinations is not None:
            self._destinations.set_base_url(base_url)
        if self._packages is not None:
            self._packages.set_base_url(base_url)
        if self._purchases is not None:
            self._purchases.set_base_url(base_url)
        if self._e_sim is not None:
            self._e_sim.set_base_url(base_url)
        if self._i_frame is not None:
            self._i_frame.set_base_url(base_url)
        if self._o_auth is not None:
            self._o_auth.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for the whole SDK, including every resource client
        already built.

        Resource clients are built lazily and cached holding a reference to the root's config, and
        both this setter and `set_retry` REBIND `_service_config` rather than mutating it -- so a
        caller who touched a resource before reconfiguring the root got a silently stale child.
        The root wins: last writer overwrites, the same rule `set_base_url` and `set_timeout`
        follow, which keeps the root and its resources in exact agreement. Narrower scopes are
        untouched, because method-level config (`set_<method>_config`) and per-call
        `request_config` live in their own attributes and are never overwritten by this. Each
        child forwards to its own sub-resources in turn.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The SDK instance.
        """
        super().set_config(config)
        if self._destinations is not None:
            self._destinations.set_config(config)
        if self._packages is not None:
            self._packages.set_config(config)
        if self._purchases is not None:
            self._purchases.set_config(config)
        if self._e_sim is not None:
            self._e_sim.set_config(config)
        if self._i_frame is not None:
            self._i_frame.set_config(config)
        if self._o_auth is not None:
            self._o_auth.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for the whole SDK, including every resource client already built.

        Resource clients are built lazily and cached with a COPY of the root's timeout baked into
        their request handler, so the inherited setter -- which only rebinds the receiver and
        rebuilds the receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The SDK instance.
        """
        super().set_timeout(timeout)
        if self._destinations is not None:
            self._destinations.set_timeout(timeout)
        if self._packages is not None:
            self._packages.set_timeout(timeout)
        if self._purchases is not None:
            self._purchases.set_timeout(timeout)
        if self._e_sim is not None:
            self._e_sim.set_timeout(timeout)
        if self._i_frame is not None:
            self._i_frame.set_timeout(timeout)
        if self._o_auth is not None:
            self._o_auth.set_timeout(timeout)

        return self

    def set_http_client(self, http_client: Optional[requests.Session]):
        """
        Sets a custom HTTP client for the whole SDK, including every resource client already
        built.

        Resource clients are built lazily and cached with a COPY of the root's http_client baked
        into their request handler, so the inherited setter -- which only rebinds the receiver and
        rebuilds the receiver's handler -- left an already-materialised child on the old client.

        :param http_client: A requests.Session-compatible client, used as-is. Pass None to fall
            back to the module-level requests API.
        :return: The SDK instance.
        """
        super().set_http_client(http_client)
        if self._destinations is not None:
            self._destinations.set_http_client(http_client)
        if self._packages is not None:
            self._packages.set_http_client(http_client)
        if self._purchases is not None:
            self._purchases.set_http_client(http_client)
        if self._e_sim is not None:
            self._e_sim.set_http_client(http_client)
        if self._i_frame is not None:
            self._i_frame.set_http_client(http_client)
        if self._o_auth is not None:
            self._o_auth.set_http_client(http_client)
        self._token_manager.set_http_client(http_client)

        return self

    def set_follow_redirects(self, follow_redirects: bool):
        """
        Sets whether HTTP redirects (3xx responses) are followed automatically, for the whole
        SDK, including every resource client already built.

        :param bool follow_redirects: False to return a 3xx response as-is instead of following it.
        :return: The SDK instance.
        """
        super().set_follow_redirects(follow_redirects)
        if self._destinations is not None:
            self._destinations.set_follow_redirects(follow_redirects)
        if self._packages is not None:
            self._packages.set_follow_redirects(follow_redirects)
        if self._purchases is not None:
            self._purchases.set_follow_redirects(follow_redirects)
        if self._e_sim is not None:
            self._e_sim.set_follow_redirects(follow_redirects)
        if self._i_frame is not None:
            self._i_frame.set_follow_redirects(follow_redirects)
        if self._o_auth is not None:
            self._o_auth.set_follow_redirects(follow_redirects)
        self._token_manager.set_follow_redirects(follow_redirects)

        return self

    def set_logging(self, logger: Optional[logging.Logger]):
        """
        Sets the logger requests/responses are written to, for the whole SDK, including every
        resource client already built.

        :param logger: A standard library logger. Pass None (the default) to disable logging.
            Authorization and Cookie header values are always redacted from logged output.
        :return: The SDK instance.
        """
        super().set_logging(logger)
        if self._destinations is not None:
            self._destinations.set_logging(logger)
        if self._packages is not None:
            self._packages.set_logging(logger)
        if self._purchases is not None:
            self._purchases.set_logging(logger)
        if self._e_sim is not None:
            self._e_sim.set_logging(logger)
        if self._i_frame is not None:
            self._i_frame.set_logging(logger)
        if self._o_auth is not None:
            self._o_auth.set_logging(logger)
        self._token_manager.set_logging(logger)

        return self

    @property
    def destinations(self) -> "DestinationsClient":
        """Lazily construct and return the destinations resource client."""
        if self._destinations is None:
            from .destinations.client import DestinationsClient

            _child = DestinationsClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._destinations = _child
        return self._destinations

    @property
    def packages(self) -> "PackagesClient":
        """Lazily construct and return the packages resource client."""
        if self._packages is None:
            from .packages.client import PackagesClient

            _child = PackagesClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._packages = _child
        return self._packages

    @property
    def purchases(self) -> "PurchasesClient":
        """Lazily construct and return the purchases resource client."""
        if self._purchases is None:
            from .purchases.client import PurchasesClient

            _child = PurchasesClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._purchases = _child
        return self._purchases

    @property
    def e_sim(self) -> "ESimClient":
        """Lazily construct and return the e_sim resource client."""
        if self._e_sim is None:
            from .e_sim.client import ESimClient

            _child = ESimClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._e_sim = _child
        return self._e_sim

    @property
    def i_frame(self) -> "IFrameClient":
        """Lazily construct and return the i_frame resource client."""
        if self._i_frame is None:
            from .i_frame.client import IFrameClient

            _child = IFrameClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._i_frame = _child
        return self._i_frame

    @property
    def o_auth(self) -> "OAuthClient":
        """Lazily construct and return the o_auth resource client."""
        if self._o_auth is None:
            from .o_auth.client import OAuthClient

            _child = OAuthClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._o_auth = _child
        return self._o_auth

    @property
    def with_raw_response(self) -> "RawCelitech":
        """
        Returns a raw-response client whose methods mirror this client's ROOT endpoints but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of the bare
        deserialized body. Resource clients expose their own `with_raw_response`.
        """
        return RawCelitech(self)


class RawCelitech:
    """
    Raw-response client for Celitech's root endpoints.

    Each method delegates to the matching :class:`Celitech` method and wraps the result in an
    ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and ``.headers``.
    A fully-grouped spec binds nothing to the root, so this is then a bare shell and the endpoints
    are reached through each resource client's own raw client.
    """

    def __init__(self, client: Celitech):
        self._client = client


class AsyncCelitech(Celitech):
    """
    Async SDK client for Celitech. Mirrors the sync client with awaitable endpoints and async
    resource accessors.
    """

    @property
    def destinations(self) -> "AsyncDestinationsClient":
        """Lazily construct and return the async destinations resource client."""
        if self._destinations is None:
            from .destinations.client import AsyncDestinationsClient

            _child = AsyncDestinationsClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._destinations = _child
        return self._destinations

    @property
    def packages(self) -> "AsyncPackagesClient":
        """Lazily construct and return the async packages resource client."""
        if self._packages is None:
            from .packages.client import AsyncPackagesClient

            _child = AsyncPackagesClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._packages = _child
        return self._packages

    @property
    def purchases(self) -> "AsyncPurchasesClient":
        """Lazily construct and return the async purchases resource client."""
        if self._purchases is None:
            from .purchases.client import AsyncPurchasesClient

            _child = AsyncPurchasesClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._purchases = _child
        return self._purchases

    @property
    def e_sim(self) -> "AsyncESimClient":
        """Lazily construct and return the async e_sim resource client."""
        if self._e_sim is None:
            from .e_sim.client import AsyncESimClient

            _child = AsyncESimClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._e_sim = _child
        return self._e_sim

    @property
    def i_frame(self) -> "AsyncIFrameClient":
        """Lazily construct and return the async i_frame resource client."""
        if self._i_frame is None:
            from .i_frame.client import AsyncIFrameClient

            _child = AsyncIFrameClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._i_frame = _child
        return self._i_frame

    @property
    def o_auth(self) -> "AsyncOAuthClient":
        """Lazily construct and return the async o_auth resource client."""
        if self._o_auth is None:
            from .o_auth.client import AsyncOAuthClient

            _child = AsyncOAuthClient(
                base_url=self.base_url, token_manager=self._token_manager
            )
            _child._default_headers = self._default_headers.copy()
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._o_auth = _child
        return self._o_auth

    @property
    def with_raw_response(self) -> "AsyncRawCelitech":
        """
        Returns an async raw-response client whose methods mirror this client's ROOT endpoints but
        return ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawCelitech(self)


class AsyncRawCelitech:
    """
    Async raw-response client for AsyncCelitech's root endpoints.
    """

    def __init__(self, client: AsyncCelitech):
        self._client = client
