from typing import Generator, Optional, Tuple

from ...oauth.token_manager import OauthToken, TokenManager
from ...transport.request import Request
from ...transport.request_error import RequestError
from ...transport.response import Response
from .base_handler import BaseHandler


class OauthHandler(BaseHandler):
    """
    Handler for OAuth token management in the request chain.
    Automatically acquires and injects OAuth tokens into requests that require authentication.

    :ivar TokenManager _token_manager: The token manager for acquiring OAuth tokens.
    """

    def __init__(self, token_manager: TokenManager):
        """
        Initialize a new instance of OauthHandler.

        :param token_manager: The token manager for acquiring OAuth tokens.
        """
        super().__init__()
        self._token_manager = token_manager

    def handle(
        self, request: Request
    ) -> Tuple[Optional[Response], Optional[RequestError]]:
        """
        Handle a request by injecting OAuth token if required.
        If the request specifies scopes, acquires a token and adds it to the Authorization header.

        :param request: The request to handle.
        :return: The response and any error that occurred.
        :raises RequestError: If the handler chain is incomplete.
        """
        if self._next_handler is None:
            raise RequestError("Handler chain is incomplete")

        if request.scopes is None:
            # This endpoint is not using Oauth
            return self._next_handler.handle(request)

        token = self._token_manager.get_token(request.scopes)
        self._update_token(request, token)

        return self._next_handler.handle(request)

    def stream(
        self, request: Request
    ) -> Generator[Tuple[Optional[Response], Optional[RequestError]], None, None]:
        """
        Handle a streaming request by injecting OAuth token if required.
        If the request specifies scopes, acquires a token and adds it to the Authorization header.

        :param request: The request to stream.
        :return: A generator yielding responses and any errors that occurred.
        :raises RequestError: If the handler chain is incomplete.
        """
        if self._next_handler is None:
            raise RequestError("Handler chain is incomplete")

        if request.scopes is None:
            # This endpoint is not using Oauth
            for response, error in self._next_handler.stream(request):
                yield response, error

        token = self._token_manager.get_token(request.scopes)
        self._update_token(request, token)

        for response, error in self._next_handler.stream(request):
            yield response, error

    def _update_token(self, request: Request, token: OauthToken):
        """
        Update the request with the OAuth token by adding it to the Authorization header.

        :param request: The request to update.
        :param token: The OAuth token to inject.
        """
        request.headers["Authorization"] = f"Bearer {token.access_token}"
