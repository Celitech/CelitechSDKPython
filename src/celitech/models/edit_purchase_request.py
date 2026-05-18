from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class EditPurchaseRequest(BaseModel):
    """EditPurchaseRequest

    :param purchase_id: ID of the purchase
    :type purchase_id: str
    :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.
    :type start_date: str
    :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.
    :type end_date: str
    :param start_time: Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months., defaults to None
    :type start_time: float, optional
    :param end_time: Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time., defaults to None
    :type end_time: float, optional
    """

    purchase_id: str = Field(
        alias="purchaseId",
        serialization_alias="purchaseId",
        description="ID of the purchase",
    )
    start_date: str = Field(
        alias="startDate",
        serialization_alias="startDate",
        description="Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.",
    )
    end_date: str = Field(
        alias="endDate",
        serialization_alias="endDate",
        description="End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.",
    )
    start_time: Optional[float] = Field(
        alias="startTime",
        serialization_alias="startTime",
        default=None,
        description="Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.",
    )
    end_time: Optional[float] = Field(
        alias="endTime",
        serialization_alias="endTime",
        default=None,
        description="Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.",
    )
