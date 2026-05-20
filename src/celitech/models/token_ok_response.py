from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class TokenOkResponse(BaseModel):
    """TokenOkResponse

    :param token: The generated token
    :type token: str
    """

    token: str = Field(description="The generated token")
