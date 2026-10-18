from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SuspendEsimOkResponse(BaseModel):
    """SuspendEsimOkResponse

    :param message: Confirmation message
    :type message: str
    """

    message: str = Field(description="Confirmation message")
