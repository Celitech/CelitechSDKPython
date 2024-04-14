import requests

from requests.exceptions import Timeout
from typing import Optional, Tuple
from .base_handler import BaseHandler
from ...transport.request import Request
from ...transport.response import Response
from ...transport.request_error import RequestError


class HttpHandler(BaseHandler):
    """
    Handler for making HTTP requests.
    This handler sends the request to the specified URL and returns the response.

    :ivar int _timeout_in_seconds: The timeout for the HTTP request in seconds.
    """

    def __init__(self):
        """
        Initialize a new instance of HttpHandler.
        """
        super().__init__()
        self._timeout_in_seconds = 60

    def handle(
        self, request: Request
    ) -> Tuple[Optional[Response], Optional[RequestError]]:
        """
        Send the request to the specified URL and return the response.

        :param Request request: The request to send.
        :return: The response and any error that occurred.
        :rtype: Tuple[Optional[Response], Optional[RequestError]]
        """
        try:
            request_args = self._get_request_data(request)

            result = requests.request(
                request.method,
                request.url,
                headers=request.headers,
                timeout=self._timeout_in_seconds,
                **request_args,
            )
            response = Response(result)

            if response.status >= 400:
                return None, RequestError(
                    message=f"{response.status} error in request to: {request.url}",
                    status=response.status,
                    response=response,
                )

            return response, None
        except Timeout:
            return None, RequestError("Request timed out")

    def _get_request_data(self, request: Request) -> dict:
        """
        Get the request arguments based on the request headers and data.

        :param Request request: The request object.
        :return: The request arguments.
        :rtype: dict
        """
        headers = request.headers or {}
        data = request.body or {}
        content_type = headers.get("Content-Type", "application/json")

        if request.method == "GET" and not data:
            return {}

        if content_type.startswith("application/") and "json" in content_type:
            return {"json": data}

        if "multipart/form-data" in content_type:
            return {"files": data}

        return {"data": data}
