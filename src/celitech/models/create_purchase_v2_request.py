from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "data_limit_in_gb": "dataLimitInGB",
        "reference_id": "referenceId",
        "network_brand": "networkBrand",
        "email_brand": "emailBrand",
    }
)
class CreatePurchaseV2Request(BaseModel):
    """CreatePurchaseV2Request

    :param destination: ISO representation of the package's destination
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
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        **kwargs
    ):
        """CreatePurchaseV2Request

        :param destination: ISO representation of the package's destination
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
