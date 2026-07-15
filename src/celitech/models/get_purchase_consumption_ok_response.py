from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class GetPurchaseConsumptionOkResponse(BaseModel):
    """GetPurchaseConsumptionOkResponse

    :param data_usage_remaining_in_bytes: Remaining balance of the package in bytes. Returns `-1` for unlimited packages.
    :type data_usage_remaining_in_bytes: float
    :param data_usage_remaining_in_gb: Remaining balance of the package in GB. Returns `-1` for unlimited packages.
    :type data_usage_remaining_in_gb: float
    :param status: Status of the connectivity, possible values are 'ACTIVE' or 'NOT_ACTIVE'
    :type status: str
    """

    data_usage_remaining_in_bytes: float = Field(
        alias="dataUsageRemainingInBytes",
        serialization_alias="dataUsageRemainingInBytes",
        description="Remaining balance of the package in bytes. Returns `-1` for unlimited packages.",
    )
    data_usage_remaining_in_gb: float = Field(
        alias="dataUsageRemainingInGB",
        serialization_alias="dataUsageRemainingInGB",
        description="Remaining balance of the package in GB. Returns `-1` for unlimited packages.",
    )
    status: str = Field(
        description="Status of the connectivity, possible values are 'ACTIVE' or 'NOT_ACTIVE'"
    )
