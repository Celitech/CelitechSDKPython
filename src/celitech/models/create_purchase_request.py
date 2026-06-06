from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class CreatePurchaseRequest(BaseModel):
    """CreatePurchaseRequest

    :param destination: destination, defaults to None
    :type destination: str, optional
    :param data_limit_in_gb: data_limit_in_gb, defaults to None
    :type data_limit_in_gb: float, optional
    :param start_date: start_date, defaults to None
    :type start_date: str, optional
    :param end_date: end_date, defaults to None
    :type end_date: str, optional
    :param email: email, defaults to None
    :type email: str, optional
    :param reference_id: reference_id, defaults to None
    :type reference_id: str, optional
    :param network_brand: network_brand, defaults to None
    :type network_brand: str, optional
    :param email_brand: email_brand, defaults to None
    :type email_brand: str, optional
    :param language: language, defaults to None
    :type language: str, optional
    :param start_time: start_time, defaults to None
    :type start_time: float, optional
    :param end_time: end_time, defaults to None
    :type end_time: float, optional
    """

    destination: Optional[str] = Field(default=None)
    data_limit_in_gb: Optional[float] = Field(
        alias="dataLimitInGB", serialization_alias="dataLimitInGB", default=None
    )
    start_date: Optional[str] = Field(
        alias="startDate", serialization_alias="startDate", default=None
    )
    end_date: Optional[str] = Field(
        alias="endDate", serialization_alias="endDate", default=None
    )
    email: Optional[str] = Field(default=None)
    reference_id: Optional[str] = Field(
        alias="referenceId", serialization_alias="referenceId", default=None
    )
    network_brand: Optional[str] = Field(
        alias="networkBrand", serialization_alias="networkBrand", default=None
    )
    email_brand: Optional[str] = Field(
        alias="emailBrand", serialization_alias="emailBrand", default=None
    )
    language: Optional[str] = Field(default=None)
    start_time: Optional[float] = Field(
        alias="startTime", serialization_alias="startTime", default=None
    )
    end_time: Optional[float] = Field(
        alias="endTime", serialization_alias="endTime", default=None
    )
