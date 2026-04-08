from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class CreatePurchaseV2Request(BaseModel):
    """CreatePurchaseV2Request

    :param destination: ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.
    :type destination: str
    :param data_limit_in_gb: Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB
    :type data_limit_in_gb: float
    :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months., defaults to None
    :type start_date: str, optional
    :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date., defaults to None
    :type end_date: str, optional
    :param duration: Duration of the package in days. Available values are 1, 2, 7, 14, 30, or 90. Either provide startDate/endDate or duration., defaults to None
    :type duration: float, optional
    :param quantity: Number of eSIMs to purchase.
    :type quantity: float
    :param email: Email address where the purchase confirmation email will be sent (including QR Code & activation steps), defaults to None
    :type email: str, optional
    :param reference_id: An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes., defaults to None
    :type reference_id: str, optional
    :param network_brand: Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters, numbers, dots (.), ampersands (&), and spaces. This feature is available to platforms with Diamond tier only., defaults to None
    :type network_brand: str, optional
    :param email_brand: Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only., defaults to None
    :type email_brand: str, optional
    """

    destination: str = Field(
        description="ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes."
    )
    data_limit_in_gb: float = Field(
        alias="dataLimitInGB",
        serialization_alias="dataLimitInGB",
        description="Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB",
    )
    start_date: Optional[str] = Field(
        alias="startDate",
        serialization_alias="startDate",
        default=None,
        description="Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.",
    )
    end_date: Optional[str] = Field(
        alias="endDate",
        serialization_alias="endDate",
        default=None,
        description="End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.",
    )
    duration: Optional[float] = Field(
        default=None,
        description="Duration of the package in days. Available values are 1, 2, 7, 14, 30, or 90. Either provide startDate/endDate or duration.",
    )
    quantity: float = Field(description="Number of eSIMs to purchase.", ge=1, le=5)
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
