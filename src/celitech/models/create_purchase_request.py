from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class CreatePurchaseRequest(BaseModel):
    """CreatePurchaseRequest

    :param destination: ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.
    :type destination: str
    :param data_limit_in_gb: Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB
    :type data_limit_in_gb: float
    :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.
    :type start_date: str
    :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.
    :type end_date: str
    :param email: Email address where the purchase confirmation email will be sent (including QR Code & activation steps), defaults to None
    :type email: str, optional
    :param reference_id: An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes., defaults to None
    :type reference_id: str, optional
    :param network_brand: Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters, numbers, dots (.), ampersands (&), and spaces. This feature is available to platforms with Diamond tier only., defaults to None
    :type network_brand: str, optional
    :param email_brand: Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only., defaults to None
    :type email_brand: str, optional
    :param start_time: Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months., defaults to None
    :type start_time: float, optional
    :param end_time: Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time., defaults to None
    :type end_time: float, optional
    """

    destination: str = Field(
        description="ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes."
    )
    data_limit_in_gb: float = Field(
        alias="dataLimitInGB",
        serialization_alias="dataLimitInGB",
        description="Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB",
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
    email: Optional[str] = Field(
        default=None,
        description="Email address where the purchase confirmation email will be sent (including QR Code & activation steps)",
    )
    reference_id: Optional[str] = Field(
        alias="referenceId",
        serialization_alias="referenceId",
        default=None,
        description="An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes.",
    )
    network_brand: Optional[str] = Field(
        alias="networkBrand",
        serialization_alias="networkBrand",
        default=None,
        description="Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters, numbers, dots (.), ampersands (&), and spaces. This feature is available to platforms with Diamond tier only.",
    )
    email_brand: Optional[str] = Field(
        alias="emailBrand",
        serialization_alias="emailBrand",
        default=None,
        description="Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only.",
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
