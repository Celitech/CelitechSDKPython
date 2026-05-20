from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class EditPurchaseOkResponse(BaseModel):
    """EditPurchaseOkResponse

    :param purchase_id: ID of the purchase
    :type purchase_id: str
    :param new_start_date: Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type new_start_date: str
    :param new_end_date: End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type new_end_date: str
    :param new_start_time: Epoch value representing the new start time of the package's validity, defaults to None
    :type new_start_time: float, optional
    :param new_end_time: Epoch value representing the new end time of the package's validity, defaults to None
    :type new_end_time: float, optional
    """

    purchase_id: str = Field(
        alias="purchaseId",
        serialization_alias="purchaseId",
        description="ID of the purchase",
    )
    new_start_date: Optional[str] = Field(
        alias="newStartDate",
        serialization_alias="newStartDate",
        description="Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    new_end_date: Optional[str] = Field(
        alias="newEndDate",
        serialization_alias="newEndDate",
        description="End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    new_start_time: Optional[float] = Field(
        alias="newStartTime",
        serialization_alias="newStartTime",
        default=None,
        description="Epoch value representing the new start time of the package's validity",
    )
    new_end_time: Optional[float] = Field(
        alias="newEndTime",
        serialization_alias="newEndTime",
        default=None,
        description="Epoch value representing the new end time of the package's validity",
    )
