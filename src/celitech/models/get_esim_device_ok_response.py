from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class Device(BaseModel):
    """Device

    :param oem: Name of the OEM
    :type oem: str
    :param hardware_name: Name of the Device
    :type hardware_name: str
    :param hardware_model: Model of the Device
    :type hardware_model: str
    :param eid: Serial Number of the eSIM
    :type eid: str
    """

    oem: str = Field(description="Name of the OEM")
    hardware_name: str = Field(
        alias="hardwareName",
        serialization_alias="hardwareName",
        description="Name of the Device",
    )
    hardware_model: str = Field(
        alias="hardwareModel",
        serialization_alias="hardwareModel",
        description="Model of the Device",
    )
    eid: str = Field(description="Serial Number of the eSIM")


class GetEsimDeviceOkResponse(BaseModel):
    """GetEsimDeviceOkResponse

    :param device: device
    :type device: Device
    """

    device: Device
