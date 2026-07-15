from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TokenOkResponse(BaseModel):
    """TokenOkResponse

    :param token: The generated token
    :type token: str
    """

    token: str = Field(description="The generated token")
