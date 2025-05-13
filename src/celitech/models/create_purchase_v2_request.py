from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "start_date": "startDate",
        "end_date": "endDate",
        "data_limit_in_gb": "dataLimitInGB",
        "reference_id": "referenceId",
        "network_brand": "networkBrand",
        "email_brand": "emailBrand",
    }
)
class CreatePurchaseV2Request(BaseModel):
    """CreatePurchaseV2Request

    :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months., defaults to None
    :type start_date: str, optional
    :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date., defaults to None
    :type end_date: str, optional
    :param duration: It designates the number of days the eSIM is valid for within the 90-day validity period from the issuance date.   For **limited packages**, the supported durations are: **1, 2, 7, 14, 30, 90 days**.   For **unlimited packages**, all durations are supported **except 90 days**. , defaults to None
    :type duration: float, optional
    :param destination: ISO representation of the package's destination.
    :type destination: str
    :param data_limit_in_gb: Size of the package in GB. For **limited packages**, the available options are: **0.5, 1, 2, 3, 5, 8, 20GB** (supports `duration` or `startDate` / `endDate`). For **unlimited packages** (available to Region-3), please use **-1** as an identifier (supports `duration` only).
    :type data_limit_in_gb: float
    :param quantity: Number of eSIMs to purchase.
    :type quantity: float
    :param email: Email address where the purchase confirmation email will be sent (including QR Code & activation steps), defaults to None
    :type email: str, optional
    :param reference_id: An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes., defaults to None
    :type reference_id: str, optional
    :param network_brand: Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters and numbers. This feature is available to platforms with Diamond tier only., defaults to None
    :type network_brand: str, optional
    :param email_brand: Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only., defaults to None
    :type email_brand: str, optional
    """

    def __init__(
        self,
        destination: str,
        data_limit_in_gb: float,
        quantity: float,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        **kwargs
    ):
        """CreatePurchaseV2Request

        :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months., defaults to None
        :type start_date: str, optional
        :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date., defaults to None
        :type end_date: str, optional
        :param duration: It designates the number of days the eSIM is valid for within the 90-day validity period from the issuance date.   For **limited packages**, the supported durations are: **1, 2, 7, 14, 30, 90 days**.   For **unlimited packages**, all durations are supported **except 90 days**. , defaults to None
        :type duration: float, optional
        :param destination: ISO representation of the package's destination.
        :type destination: str
        :param data_limit_in_gb: Size of the package in GB. For **limited packages**, the available options are: **0.5, 1, 2, 3, 5, 8, 20GB** (supports `duration` or `startDate` / `endDate`). For **unlimited packages** (available to Region-3), please use **-1** as an identifier (supports `duration` only).
        :type data_limit_in_gb: float
        :param quantity: Number of eSIMs to purchase.
        :type quantity: float
        :param email: Email address where the purchase confirmation email will be sent (including QR Code & activation steps), defaults to None
        :type email: str, optional
        :param reference_id: An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes., defaults to None
        :type reference_id: str, optional
        :param network_brand: Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters and numbers. This feature is available to platforms with Diamond tier only., defaults to None
        :type network_brand: str, optional
        :param email_brand: Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only., defaults to None
        :type email_brand: str, optional
        """
        self.start_date = self._define_str("start_date", start_date, nullable=True)
        self.end_date = self._define_str("end_date", end_date, nullable=True)
        self.duration = self._define_number("duration", duration, nullable=True)
        self.destination = destination
        self.data_limit_in_gb = data_limit_in_gb
        self.quantity = self._define_number("quantity", quantity, ge=1, le=5)
        self.email = self._define_str("email", email, nullable=True)
        self.reference_id = self._define_str(
            "reference_id", reference_id, nullable=True
        )
        self.network_brand = self._define_str(
            "network_brand", network_brand, nullable=True
        )
        self.email_brand = self._define_str("email_brand", email_brand, nullable=True)
        self._kwargs = kwargs
