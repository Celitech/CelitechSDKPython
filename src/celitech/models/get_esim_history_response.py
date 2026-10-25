from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class GetEsimHistoryResponseEsimHistoryItem(BaseModel):
    """GetEsimHistoryResponseEsimHistoryItem

    :param status: The status of the eSIM at a given time, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR'
    :type status: str
    :param status_date: The date when the eSIM status changed in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type status_date: str
    :param date: Epoch value representing the date when the eSIM status changed, defaults to None
    :type date: float, optional
    """

    status: str = Field(
        description="The status of the eSIM at a given time, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR'"
    )
    status_date: str = Field(
        alias="statusDate",
        serialization_alias="statusDate",
        description="The date when the eSIM status changed in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    date: Optional[float] = Field(
        default=None,
        description="Epoch value representing the date when the eSIM status changed",
    )


class GetEsimHistoryResponseEsim(BaseModel):
    """GetEsimHistoryResponseEsim

    :param iccid: ID of the eSIM
    :type iccid: str
    :param history: history
    :type history: List[GetEsimHistoryResponseEsimHistoryItem]
    """

    iccid: str = Field(description="ID of the eSIM")
    history: List[GetEsimHistoryResponseEsimHistoryItem]


class GetEsimHistoryResponse(BaseModel):
    """GetEsimHistoryResponse

    :param esim: esim
    :type esim: GetEsimHistoryResponseEsim
    """

    esim: GetEsimHistoryResponseEsim
