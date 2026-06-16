from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class EditPurchaseRequest(BaseModel):
    """EditPurchaseRequest

    :param purchase_id: purchase_id, defaults to None
    :type purchase_id: str, optional
    :param start_date: start_date, defaults to None
    :type start_date: str, optional
    :param end_date: end_date, defaults to None
    :type end_date: str, optional
    :param start_time: start_time, defaults to None
    :type start_time: float, optional
    :param end_time: end_time, defaults to None
    :type end_time: float, optional
    """

    purchase_id: Optional[str] = Field(
        alias="purchaseId", serialization_alias="purchaseId", default=None
    )
    start_date: Optional[str] = Field(
        alias="startDate", serialization_alias="startDate", default=None
    )
    end_date: Optional[str] = Field(
        alias="endDate", serialization_alias="endDate", default=None
    )
    start_time: Optional[float] = Field(
        alias="startTime", serialization_alias="startTime", default=None
    )
    end_time: Optional[float] = Field(
        alias="endTime", serialization_alias="endTime", default=None
    )
