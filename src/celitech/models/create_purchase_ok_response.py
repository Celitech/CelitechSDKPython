from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class CreatePurchaseOkResponsePurchase(BaseModel):
    """CreatePurchaseOkResponsePurchase

    :param id_: ID of the purchase
    :type id_: str
    :param package_id: ID of the package
    :type package_id: str
    :param start_date: Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type start_date: str
    :param end_date: End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type end_date: str
    :param created_date: Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type created_date: str
    :param start_time: Epoch value representing the start time of the package's validity, defaults to None
    :type start_time: float, optional
    :param end_time: Epoch value representing the end time of the package's validity, defaults to None
    :type end_time: float, optional
    """

    id_: str = Field(
        alias="id", serialization_alias="id", description="ID of the purchase"
    )
    package_id: str = Field(
        alias="packageId",
        serialization_alias="packageId",
        description="ID of the package",
    )
    start_date: Optional[str] = Field(
        alias="startDate",
        serialization_alias="startDate",
        description="Start date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    end_date: Optional[str] = Field(
        alias="endDate",
        serialization_alias="endDate",
        description="End date of the package's validity in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    created_date: str = Field(
        alias="createdDate",
        serialization_alias="createdDate",
        description="Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )
    start_time: Optional[float] = Field(
        alias="startTime",
        serialization_alias="startTime",
        default=None,
        description="Epoch value representing the start time of the package's validity",
    )
    end_time: Optional[float] = Field(
        alias="endTime",
        serialization_alias="endTime",
        default=None,
        description="Epoch value representing the end time of the package's validity",
    )


class CreatePurchaseOkResponseProfile(BaseModel):
    """CreatePurchaseOkResponseProfile

    :param iccid: ID of the eSIM
    :type iccid: str
    :param activation_code: QR Code of the eSIM as base64
    :type activation_code: str
    :param manual_activation_code: Manual Activation Code of the eSIM
    :type manual_activation_code: str
    """

    iccid: str = Field(description="ID of the eSIM", min_length=18, max_length=22)
    activation_code: str = Field(
        alias="activationCode",
        serialization_alias="activationCode",
        description="QR Code of the eSIM as base64",
        min_length=1000,
        max_length=8000,
    )
    manual_activation_code: str = Field(
        alias="manualActivationCode",
        serialization_alias="manualActivationCode",
        description="Manual Activation Code of the eSIM",
    )


class CreatePurchaseOkResponse(BaseModel):
    """CreatePurchaseOkResponse

    :param purchase: purchase
    :type purchase: CreatePurchaseOkResponsePurchase
    :param profile: profile
    :type profile: CreatePurchaseOkResponseProfile
    """

    purchase: CreatePurchaseOkResponsePurchase
    profile: CreatePurchaseOkResponseProfile
