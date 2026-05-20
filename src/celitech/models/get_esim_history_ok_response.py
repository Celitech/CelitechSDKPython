from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class History(BaseModel):
    """History

    :param status: The status of the eSIM at a given time, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR'
    :type status: str
    :param status_date: The date when the eSIM status changed in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type status_date: str
    :param date_: Epoch value representing the date when the eSIM status changed, defaults to None
    :type date_: float, optional
    """

    status: str = Field(
        description="The status of the eSIM at a given time, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR'"
    )
    status_date: str = Field(
        alias="statusDate",
        serialization_alias="statusDate",
        description="The date when the eSIM status changed in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    date_: Optional[float] = Field(
        alias="date",
        serialization_alias="date",
        default=None,
        description="Epoch value representing the date when the eSIM status changed",
    )


class GetEsimHistoryOkResponseEsim(BaseModel):
    """GetEsimHistoryOkResponseEsim

    :param iccid: ID of the eSIM
    :type iccid: str
    :param history: history
    :type history: List[History]
    """

    iccid: str = Field(description="ID of the eSIM", min_length=18, max_length=22)
    history: List[History]


class GetEsimHistoryOkResponse(BaseModel):
    """GetEsimHistoryOkResponse

    :param esim: esim
    :type esim: GetEsimHistoryOkResponseEsim
    """

    esim: GetEsimHistoryOkResponseEsim
