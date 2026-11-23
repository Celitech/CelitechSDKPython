from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_error import BaseError
from .utils.base_model import BaseModel


# Pydantic validation model for ErrorResponse
class ErrorResponseData(BaseModel):
    """ErrorResponse

    :param message: Message of the error, defaults to None
    :type message: str, optional
    """

    message: Optional[str] = Field(default=None, description="Message of the error")


# Error exception class
class ErrorResponse(BaseError):
    """ErrorResponse

    :param message: Message of the error, defaults to None
    :type message: str, optional
    """

    _model_class = ErrorResponseData
