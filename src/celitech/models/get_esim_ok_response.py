from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class GetEsimOkResponseEsim(BaseModel):
    """GetEsimOkResponseEsim

    :param iccid: ID of the eSIM
    :type iccid: str
    :param smdp_address: SM-DP+ Address
    :type smdp_address: str
    :param activation_code: QR Code of the eSIM as base64
    :type activation_code: str
    :param manual_activation_code: The manual activation code
    :type manual_activation_code: str
    :param status: Status of the eSIM, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR'
    :type status: str
    :param connectivity_status: Status of the eSIM connectivity, possible values are 'ACTIVE' or 'NOT_ACTIVE'
    :type connectivity_status: str
    :param is_top_up_allowed: Indicates whether the eSIM is currently eligible for a top-up. This flag should be checked before attempting a top-up request.
    :type is_top_up_allowed: bool
    """

    iccid: str = Field(description="ID of the eSIM", min_length=18, max_length=22)
    smdp_address: str = Field(
        alias="smdpAddress",
        serialization_alias="smdpAddress",
        description="SM-DP+ Address",
    )
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
        description="The manual activation code",
    )
    status: str = Field(
        description="Status of the eSIM, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR'"
    )
    connectivity_status: str = Field(
        alias="connectivityStatus",
        serialization_alias="connectivityStatus",
        description="Status of the eSIM connectivity, possible values are 'ACTIVE' or 'NOT_ACTIVE'",
    )
    is_top_up_allowed: bool = Field(
        alias="isTopUpAllowed",
        serialization_alias="isTopUpAllowed",
        description="Indicates whether the eSIM is currently eligible for a top-up. This flag should be checked before attempting a top-up request.",
    )


class GetEsimOkResponse(BaseModel):
    """GetEsimOkResponse

    :param esim: esim
    :type esim: GetEsimOkResponseEsim
    """

    esim: GetEsimOkResponseEsim
