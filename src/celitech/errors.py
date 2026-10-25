# The two transport-failure types are re-exported, not defined here: this module holds the classes
# named for a RESPONSE status, and neither a timeout (FSDK-1585) nor a failed connection
# (FSDK-1573) has one. Importing them keeps `from <sdk>.errors import ...` the one place a caller
# looks for the SDK's error types.
from .net.transport.api_error import ApiConnectionError, ApiError, ApiTimeoutError
from typing import Any, Dict, Optional, Type


class BadRequestError(ApiError):
    """Raised on HTTP 400 responses."""

    def __init__(self, body: Any = None, headers: Optional[Dict[str, str]] = None):
        super().__init__(
            status=400,
            status_code=400,
            headers=headers,
            body=body,
        )


class UnauthorizedError(ApiError):
    """Raised on HTTP 401 responses."""

    def __init__(self, body: Any = None, headers: Optional[Dict[str, str]] = None):
        super().__init__(
            status=401,
            status_code=401,
            headers=headers,
            body=body,
        )


class ConflictError(ApiError):
    """Raised on HTTP 409 responses."""

    def __init__(self, body: Any = None, headers: Optional[Dict[str, str]] = None):
        super().__init__(
            status=409,
            status_code=409,
            headers=headers,
            body=body,
        )


class UnprocessableEntityError(ApiError):
    """Raised on HTTP 422 responses."""

    def __init__(self, body: Any = None, headers: Optional[Dict[str, str]] = None):
        super().__init__(
            status=422,
            status_code=422,
            headers=headers,
            body=body,
        )


class ServiceUnavailableError(ApiError):
    """Raised on HTTP 503 responses."""

    def __init__(self, body: Any = None, headers: Optional[Dict[str, str]] = None):
        super().__init__(
            status=503,
            status_code=503,
            headers=headers,
            body=body,
        )


_STATUS_TO_ERROR: Dict[int, Type[ApiError]] = {
    400: BadRequestError,
    401: UnauthorizedError,
    409: ConflictError,
    422: UnprocessableEntityError,
    503: ServiceUnavailableError,
}


def subclass_for_code(status_code: int) -> Type[ApiError]:
    """Return the typed exception class for an HTTP status code, or ApiError if unmapped."""
    return _STATUS_TO_ERROR.get(status_code, ApiError)
