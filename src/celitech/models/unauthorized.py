from pydantic import Field
from typing import Optional
from .utils.base_error import BaseError
from .utils.base_model import BaseModel


# Pydantic validation model for Unauthorized
class UnauthorizedData(BaseModel):
    """Unauthorized

    :param message: Message of the error, defaults to None
    :type message: str, optional
    """

    message: Optional[str] = Field(default=None, description="Message of the error")


# Error exception class
class Unauthorized(BaseError):
    """Unauthorized

    :param message: Message of the error, defaults to None
    :type message: str, optional
    """

    _model_class = UnauthorizedData
