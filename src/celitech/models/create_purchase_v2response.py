from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreatePurchaseV2ResponsePurchase(BaseModel):
    """CreatePurchaseV2ResponsePurchase

    :param id: ID of the purchase
    :type id: str
    :param package_id: ID of the package
    :type package_id: str
    :param created_date: Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'
    :type created_date: str
    """

    id: str = Field(description="ID of the purchase")
    package_id: str = Field(
        alias="packageId",
        serialization_alias="packageId",
        description="ID of the package",
    )
    created_date: str = Field(
        alias="createdDate",
        serialization_alias="createdDate",
        description="Creation date of the purchase in the format 'yyyy-MM-ddThh:mm:ssZZ'",
    )


class CreatePurchaseV2ResponseProfile(BaseModel):
    """CreatePurchaseV2ResponseProfile

    :param iccid: ID of the eSIM
    :type iccid: str
    :param activation_code: QR Code of the eSIM as base64
    :type activation_code: str
    :param manual_activation_code: Manual Activation Code of the eSIM
    :type manual_activation_code: str
    :param ios_activation_link: iOS Activation Link of the eSIM
    :type ios_activation_link: str
    :param android_activation_link: Android Activation Link of the eSIM
    :type android_activation_link: str
    """

    iccid: str = Field(description="ID of the eSIM")
    activation_code: str = Field(
        alias="activationCode",
        serialization_alias="activationCode",
        description="QR Code of the eSIM as base64",
    )
    manual_activation_code: str = Field(
        alias="manualActivationCode",
        serialization_alias="manualActivationCode",
        description="Manual Activation Code of the eSIM",
    )
    ios_activation_link: str = Field(
        alias="iosActivationLink",
        serialization_alias="iosActivationLink",
        description="iOS Activation Link of the eSIM",
    )
    android_activation_link: str = Field(
        alias="androidActivationLink",
        serialization_alias="androidActivationLink",
        description="Android Activation Link of the eSIM",
    )


class CreatePurchaseV2Response(BaseModel):
    """CreatePurchaseV2Response

    :param purchase: purchase
    :type purchase: CreatePurchaseV2ResponsePurchase
    :param profile: profile
    :type profile: CreatePurchaseV2ResponseProfile
    """

    purchase: CreatePurchaseV2ResponsePurchase
    profile: CreatePurchaseV2ResponseProfile
