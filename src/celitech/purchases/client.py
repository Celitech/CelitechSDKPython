from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    CreatePurchaseRequest,
    CreatePurchaseRequestLanguage,
    CreatePurchaseResponse,
    CreatePurchaseV2Request,
    CreatePurchaseV2RequestLanguage,
    CreatePurchaseV2Response,
    EditPurchaseRequest,
    EditPurchaseResponse,
    ErrorResponse,
    GetPurchaseConsumptionResponse,
    ListPurchasesResponse,
    TopUpEsimRequest,
    TopUpEsimResponse,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class PurchasesClient(BaseService):
    """
    Fern-style resource client for PurchasesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_purchase_v2_config: SdkConfig = {}
        self._list_purchases_config: SdkConfig = {}
        self._create_purchase_config: SdkConfig = {}
        self._top_up_esim_config: SdkConfig = {}
        self._edit_purchase_config: SdkConfig = {}
        self._get_purchase_consumption_config: SdkConfig = {}

    def set_create_purchase_v2_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_purchase_v2.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_purchase_v2_config = config
        return self

    def set_list_purchases_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_purchases.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_purchases_config = config
        return self

    def set_create_purchase_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_purchase.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_purchase_config = config
        return self

    def set_top_up_esim_config(self, config: SdkConfig):
        """
        Sets method-level configuration for top_up_esim.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._top_up_esim_config = config
        return self

    def set_edit_purchase_config(self, config: SdkConfig):
        """
        Sets method-level configuration for edit_purchase.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._edit_purchase_config = config
        return self

    def set_get_purchase_consumption_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_purchase_consumption.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_purchase_consumption_config = config
        return self

    @property
    def with_raw_response(self) -> "RawPurchasesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawPurchasesClient(self)

    @cast_models
    def create_purchase_v2(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        quantity: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseV2RequestLanguage] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> List[CreatePurchaseV2Response]:
        """
        This endpoint is used to purchase a new eSIM by providing the package details.

        Parameters
        ----------
        destination : str
            ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.

        data_limit_in_gb : float
            Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB. Use `-1` to purchase an unlimited (date-based) package — provide `startDate`/`endDate` spanning 3 to 30 days (`duration` is not supported for unlimited packages).

        quantity : float
            Number of eSIMs to purchase.

        start_date : typing.Optional[str]
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : typing.Optional[str]
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        duration : typing.Optional[float]
            Duration of the package in days. Available values are 1, 2, 7, 14, 30, or 90. Either provide startDate/endDate or duration. Not supported for unlimited packages (`dataLimitInGB` = -1), which are date-based — provide startDate/endDate instead.

        email : typing.Optional[str]
            Email address where the purchase confirmation email will be sent (including QR Code & activation steps)

        reference_id : typing.Optional[str]
            An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes. Letters, digits, `-`, `_`, `.`, `@` and `+` are allowed (so an email address works), up to 255 characters.

        network_brand : typing.Optional[str]
            Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters, numbers, dots (.), ampersands (&), and spaces. This feature is available to platforms with Diamond tier only.

        email_brand : typing.Optional[str]
            Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only.

        language : typing.Optional[CreatePurchaseV2RequestLanguage]
            Language of the confirmation email sent to the customer.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreatePurchaseV2Response]
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.purchases.create_purchase_v2(
            destination="FRA",
            data_limit_in_gb=1,
            quantity=1,
        )
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._create_purchase_v2_config, request_options
        )

        request_body = CreatePurchaseV2Request(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(CreatePurchaseV2Request).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/purchases/v2",
                [],
                resolved_config,
            )
            .add_header("Idempotency-Key", idempotency_key)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            [
                CreatePurchaseV2Response.model_validate(item)
                for item in (response if isinstance(response, list) else [])
            ]
            if should_validate_response(resolved_config)
            else construct_lenient(
                List[CreatePurchaseV2Response],
                (response if isinstance(response, list) else []),
            )
        )

    @cast_models
    def list_purchases(
        self,
        *,
        purchase_id: Optional[str] = SENTINEL,
        iccid: Optional[str] = SENTINEL,
        after_date: Optional[str] = SENTINEL,
        before_date: Optional[str] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        after: Optional[float] = SENTINEL,
        before: Optional[float] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListPurchasesResponse:
        """
        This endpoint can be used to list all the successful purchases made between a given interval.

        Parameters
        ----------
        purchase_id : typing.Optional[str]
            ID of the purchase

        iccid : typing.Optional[str]
            ID of the eSIM

        after_date : typing.Optional[str]
            Start date of the interval for filtering purchases in the format 'yyyy-MM-dd'

        before_date : typing.Optional[str]
            End date of the interval for filtering purchases in the format 'yyyy-MM-dd'

        email : typing.Optional[str]
            Email associated to the purchase.

        reference_id : typing.Optional[str]
            The referenceId that was provided by the partner during the purchase or topup flow.

        after_cursor : typing.Optional[str]
            To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data.

        limit : typing.Optional[float]
            Maximum number of purchases to be returned in the response. The value must be greater than 0 and less than or equal to 100. If not provided, the default value is 20

        after : typing.Optional[float]
            Epoch value representing the start of the time interval for filtering purchases

        before : typing.Optional[float]
            Epoch value representing the end of the time interval for filtering purchases

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPurchasesResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.purchases.list_purchases()
        """

        Validator(str).is_optional().validate(purchase_id, "purchase_id")
        Validator(str).is_optional().validate(iccid, "iccid")
        Validator(str).is_optional().validate(after_date, "after_date")
        Validator(str).is_optional().validate(before_date, "before_date")
        Validator(str).is_optional().validate(email, "email")
        Validator(str).is_optional().validate(reference_id, "reference_id")
        Validator(str).is_optional().validate(after_cursor, "after_cursor")
        Validator(float).is_optional().validate(limit, "limit")
        Validator(float).is_optional().validate(after, "after")
        Validator(float).is_optional().validate(before, "before")

        resolved_config = self._get_resolved_config(
            self._list_purchases_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/purchases",
                [],
                resolved_config,
            )
            .add_query("purchaseId", purchase_id)
            .add_query("iccid", iccid)
            .add_query("afterDate", after_date)
            .add_query("beforeDate", before_date)
            .add_query("email", email)
            .add_query("referenceId", reference_id)
            .add_query("afterCursor", after_cursor)
            .add_query("limit", limit)
            .add_query("after", after)
            .add_query("before", before)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListPurchasesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListPurchasesResponse, response)
            )
        )

    @cast_models
    def create_purchase(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseRequestLanguage] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CreatePurchaseResponse:
        """
        This endpoint is used to purchase a new eSIM by providing the package details.

        Parameters
        ----------
        destination : str
            ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.

        data_limit_in_gb : float
            Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB. Use `-1` to purchase an unlimited (date-based) package — provide `startDate`/`endDate` spanning 3 to 30 days.

        start_date : str
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : str
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        email : typing.Optional[str]
            Email address where the purchase confirmation email will be sent (including QR Code & activation steps)

        reference_id : typing.Optional[str]
            An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes. Letters, digits, `-`, `_`, `.`, `@` and `+` are allowed (so an email address works), up to 255 characters.

        network_brand : typing.Optional[str]
            Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters, numbers, dots (.), ampersands (&), and spaces. This feature is available to platforms with Diamond tier only.

        email_brand : typing.Optional[str]
            Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only.

        language : typing.Optional[CreatePurchaseRequestLanguage]
            Language of the confirmation email sent to the customer.

        start_time : typing.Optional[float]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.

        end_time : typing.Optional[float]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePurchaseResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.purchases.create_purchase(
            destination="FRA",
            data_limit_in_gb=1,
            start_date="2023-11-01",
            end_date="2023-11-20",
        )
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._create_purchase_config, request_options
        )

        request_body = CreatePurchaseRequest(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                        "start_time": start_time,
                        "end_time": end_time,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(CreatePurchaseRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/purchases",
                [],
                resolved_config,
            )
            .add_header("Idempotency-Key", idempotency_key)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreatePurchaseResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreatePurchaseResponse, response)
            )
        )

    @cast_models
    def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> TopUpEsimResponse:
        """
        This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.

        Parameters
        ----------
        iccid : str
            ID of the eSIM

        data_limit_in_gb : float
            Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB. Use `-1` to top up with an unlimited (date-based) package — provide `startDate`/`endDate` spanning 3 to 30 days (`duration` is not supported for unlimited packages).

        start_date : typing.Optional[str]
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : typing.Optional[str]
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        duration : typing.Optional[float]
            Duration of the package in days. Available values are 1, 2, 7, 14, 30, or 90. Either provide startDate/endDate or duration. Not supported for unlimited packages (`dataLimitInGB` = -1), which are date-based — provide startDate/endDate instead.

        email : typing.Optional[str]
            Email address where the purchase confirmation email will be sent (excluding QR Code & activation steps).

        reference_id : typing.Optional[str]
            An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes. Letters, digits, `-`, `_`, `.`, `@` and `+` are allowed (so an email address works), up to 255 characters.

        email_brand : typing.Optional[str]
            Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only.

        start_time : typing.Optional[float]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.

        end_time : typing.Optional[float]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TopUpEsimResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.purchases.top_up_esim(
            iccid="1111222233334444555000",
            data_limit_in_gb=1,
        )
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._top_up_esim_config, request_options
        )

        request_body = TopUpEsimRequest(
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "email_brand": email_brand,
                        "start_time": start_time,
                        "end_time": end_time,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(TopUpEsimRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/purchases/topup",
                [],
                resolved_config,
            )
            .add_header("Idempotency-Key", idempotency_key)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                TopUpEsimResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(TopUpEsimResponse, response)
            )
        )

    @cast_models
    def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> EditPurchaseResponse:
        """
        This endpoint allows you to modify the validity dates of an existing purchase.

        **Behavior:**
        - If the purchase has **not yet been activated**, both the start and end dates can be updated.
        - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set).
        - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category.

        The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits.

        Parameters
        ----------
        purchase_id : str
            ID of the purchase

        start_date : str
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : str
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        start_time : typing.Optional[float]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.

        end_time : typing.Optional[float]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditPurchaseResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.purchases.edit_purchase(
            purchase_id="ae471106-c8b4-42cf-b83a-b061291f2922",
            start_date="2023-11-01",
            end_date="2023-11-20",
        )
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._edit_purchase_config, request_options
        )

        request_body = EditPurchaseRequest(
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"start_time": start_time, "end_time": end_time}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(EditPurchaseRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/purchases/edit",
                [],
                resolved_config,
            )
            .add_header("Idempotency-Key", idempotency_key)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EditPurchaseResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EditPurchaseResponse, response)
            )
        )

    @cast_models
    def get_purchase_consumption(
        self, purchase_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetPurchaseConsumptionResponse:
        """
        This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

        Parameters
        ----------
        purchase_id : str
            ID of the purchase

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPurchaseConsumptionResponse
            Successful Response

        Examples
        --------
        from celitech import Celitech

        client = Celitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )
        client.purchases.get_purchase_consumption(
            purchase_id="4973fa15-6979-4daa-9cf3-672620df819c",
        )
        """

        Validator(str).validate(purchase_id, "purchase_id")

        resolved_config = self._get_resolved_config(
            self._get_purchase_consumption_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or CelitechEnvironment.DEFAULT.url}/purchases/{{purchaseId}}/consumption",
                [],
                resolved_config,
            )
            .add_path("purchaseId", purchase_id)
            .add_error(400, ErrorResponse)
            .add_error(401, ErrorResponse)
            .add_error(409, ErrorResponse)
            .add_error(422, ErrorResponse)
            .add_error(503, ErrorResponse)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetPurchaseConsumptionResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetPurchaseConsumptionResponse, response)
            )
        )


class RawPurchasesClient:
    """
    Raw-response client for PurchasesClient.

    Each method delegates to the matching :class:`PurchasesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: PurchasesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create_purchase_v2(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        quantity: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseV2RequestLanguage] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[List[CreatePurchaseV2Response]]:
        data = PurchasesClient.create_purchase_v2(
            self._client,
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def list_purchases(
        self,
        *,
        purchase_id: Optional[str] = SENTINEL,
        iccid: Optional[str] = SENTINEL,
        after_date: Optional[str] = SENTINEL,
        before_date: Optional[str] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        after: Optional[float] = SENTINEL,
        before: Optional[float] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPurchasesResponse]:
        data = PurchasesClient.list_purchases(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "purchase_id": purchase_id,
                        "iccid": iccid,
                        "after_date": after_date,
                        "before_date": before_date,
                        "email": email,
                        "reference_id": reference_id,
                        "after_cursor": after_cursor,
                        "limit": limit,
                        "after": after,
                        "before": before,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_purchase(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseRequestLanguage] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePurchaseResponse]:
        data = PurchasesClient.create_purchase(
            self._client,
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[TopUpEsimResponse]:
        data = PurchasesClient.top_up_esim(
            self._client,
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "email_brand": email_brand,
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditPurchaseResponse]:
        data = PurchasesClient.edit_purchase(
            self._client,
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_purchase_consumption(
        self, purchase_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetPurchaseConsumptionResponse]:
        data = PurchasesClient.get_purchase_consumption(
            self._client, purchase_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPurchasesClient(PurchasesClient):
    """
    Async wrapper for PurchasesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawPurchasesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPurchasesClient(self)

    def create_purchase_v2(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        quantity: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseV2RequestLanguage] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[List[CreatePurchaseV2Response]]:  # type: ignore[override]
        """
        This endpoint is used to purchase a new eSIM by providing the package details.

        Parameters
        ----------
        destination : str
            ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.

        data_limit_in_gb : float
            Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB. Use `-1` to purchase an unlimited (date-based) package — provide `startDate`/`endDate` spanning 3 to 30 days (`duration` is not supported for unlimited packages).

        quantity : float
            Number of eSIMs to purchase.

        start_date : typing.Optional[str]
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : typing.Optional[str]
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        duration : typing.Optional[float]
            Duration of the package in days. Available values are 1, 2, 7, 14, 30, or 90. Either provide startDate/endDate or duration. Not supported for unlimited packages (`dataLimitInGB` = -1), which are date-based — provide startDate/endDate instead.

        email : typing.Optional[str]
            Email address where the purchase confirmation email will be sent (including QR Code & activation steps)

        reference_id : typing.Optional[str]
            An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes. Letters, digits, `-`, `_`, `.`, `@` and `+` are allowed (so an email address works), up to 255 characters.

        network_brand : typing.Optional[str]
            Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters, numbers, dots (.), ampersands (&), and spaces. This feature is available to platforms with Diamond tier only.

        email_brand : typing.Optional[str]
            Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only.

        language : typing.Optional[CreatePurchaseV2RequestLanguage]
            Language of the confirmation email sent to the customer.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreatePurchaseV2Response]
            Successful Response

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.purchases.create_purchase_v2(
                destination="FRA",
                data_limit_in_gb=1,
                quantity=1,
            )


        asyncio.run(main())
        """
        return to_async(super().create_purchase_v2)(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def list_purchases(
        self,
        *,
        purchase_id: Optional[str] = SENTINEL,
        iccid: Optional[str] = SENTINEL,
        after_date: Optional[str] = SENTINEL,
        before_date: Optional[str] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        after: Optional[float] = SENTINEL,
        before: Optional[float] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListPurchasesResponse]:  # type: ignore[override]
        """
        This endpoint can be used to list all the successful purchases made between a given interval.

        Parameters
        ----------
        purchase_id : typing.Optional[str]
            ID of the purchase

        iccid : typing.Optional[str]
            ID of the eSIM

        after_date : typing.Optional[str]
            Start date of the interval for filtering purchases in the format 'yyyy-MM-dd'

        before_date : typing.Optional[str]
            End date of the interval for filtering purchases in the format 'yyyy-MM-dd'

        email : typing.Optional[str]
            Email associated to the purchase.

        reference_id : typing.Optional[str]
            The referenceId that was provided by the partner during the purchase or topup flow.

        after_cursor : typing.Optional[str]
            To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data.

        limit : typing.Optional[float]
            Maximum number of purchases to be returned in the response. The value must be greater than 0 and less than or equal to 100. If not provided, the default value is 20

        after : typing.Optional[float]
            Epoch value representing the start of the time interval for filtering purchases

        before : typing.Optional[float]
            Epoch value representing the end of the time interval for filtering purchases

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPurchasesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.purchases.list_purchases()


        asyncio.run(main())
        """
        return to_async(super().list_purchases)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "purchase_id": purchase_id,
                        "iccid": iccid,
                        "after_date": after_date,
                        "before_date": before_date,
                        "email": email,
                        "reference_id": reference_id,
                        "after_cursor": after_cursor,
                        "limit": limit,
                        "after": after,
                        "before": before,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create_purchase(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseRequestLanguage] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreatePurchaseResponse]:  # type: ignore[override]
        """
        This endpoint is used to purchase a new eSIM by providing the package details.

        Parameters
        ----------
        destination : str
            ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes.

        data_limit_in_gb : float
            Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB. Use `-1` to purchase an unlimited (date-based) package — provide `startDate`/`endDate` spanning 3 to 30 days.

        start_date : str
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : str
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        email : typing.Optional[str]
            Email address where the purchase confirmation email will be sent (including QR Code & activation steps)

        reference_id : typing.Optional[str]
            An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes. Letters, digits, `-`, `_`, `.`, `@` and `+` are allowed (so an email address works), up to 255 characters.

        network_brand : typing.Optional[str]
            Customize the network brand of the issued eSIM. The `networkBrand` parameter cannot exceed 15 characters in length and must contain only letters, numbers, dots (.), ampersands (&), and spaces. This feature is available to platforms with Diamond tier only.

        email_brand : typing.Optional[str]
            Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only.

        language : typing.Optional[CreatePurchaseRequestLanguage]
            Language of the confirmation email sent to the customer.

        start_time : typing.Optional[float]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.

        end_time : typing.Optional[float]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePurchaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.purchases.create_purchase(
                destination="FRA",
                data_limit_in_gb=1,
                start_date="2023-11-01",
                end_date="2023-11-20",
            )


        asyncio.run(main())
        """
        return to_async(super().create_purchase)(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[TopUpEsimResponse]:  # type: ignore[override]
        """
        This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.

        Parameters
        ----------
        iccid : str
            ID of the eSIM

        data_limit_in_gb : float
            Size of the package in GB. The available options are 0.5, 1, 2, 3, 5, 8, 20, 50GB. Use `-1` to top up with an unlimited (date-based) package — provide `startDate`/`endDate` spanning 3 to 30 days (`duration` is not supported for unlimited packages).

        start_date : typing.Optional[str]
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : typing.Optional[str]
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        duration : typing.Optional[float]
            Duration of the package in days. Available values are 1, 2, 7, 14, 30, or 90. Either provide startDate/endDate or duration. Not supported for unlimited packages (`dataLimitInGB` = -1), which are date-based — provide startDate/endDate instead.

        email : typing.Optional[str]
            Email address where the purchase confirmation email will be sent (excluding QR Code & activation steps).

        reference_id : typing.Optional[str]
            An identifier provided by the partner to link this purchase to their booking or transaction for analytics and debugging purposes. Letters, digits, `-`, `_`, `.`, `@` and `+` are allowed (so an email address works), up to 255 characters.

        email_brand : typing.Optional[str]
            Customize the email subject brand. The `emailBrand` parameter cannot exceed 25 characters in length and must contain only letters, numbers, and spaces. This feature is available to platforms with Diamond tier only.

        start_time : typing.Optional[float]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.

        end_time : typing.Optional[float]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TopUpEsimResponse
            Successful Response

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.purchases.top_up_esim(
                iccid="1111222233334444555000",
                data_limit_in_gb=1,
            )


        asyncio.run(main())
        """
        return to_async(super().top_up_esim)(
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "email_brand": email_brand,
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EditPurchaseResponse]:  # type: ignore[override]
        """
        This endpoint allows you to modify the validity dates of an existing purchase.

        **Behavior:**
        - If the purchase has **not yet been activated**, both the start and end dates can be updated.
        - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set).
        - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category.

        The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits.

        Parameters
        ----------
        purchase_id : str
            ID of the purchase

        start_date : str
            Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months.

        end_date : str
            End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date.

        start_time : typing.Optional[float]
            Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months.

        end_time : typing.Optional[float]
            Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time.

        idempotency_key : typing.Optional[str]
            Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditPurchaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.purchases.edit_purchase(
                purchase_id="ae471106-c8b4-42cf-b83a-b061291f2922",
                start_date="2023-11-01",
                end_date="2023-11-20",
            )


        asyncio.run(main())
        """
        return to_async(super().edit_purchase)(
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get_purchase_consumption(
        self, purchase_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetPurchaseConsumptionResponse]:  # type: ignore[override]
        """
        This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

        Parameters
        ----------
        purchase_id : str
            ID of the purchase

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPurchaseConsumptionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from celitech import AsyncCelitech

        client = AsyncCelitech(
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
        )


        async def main() -> None:
            await client.purchases.get_purchase_consumption(
                purchase_id="4973fa15-6979-4daa-9cf3-672620df819c",
            )


        asyncio.run(main())
        """
        return to_async(super().get_purchase_consumption)(
            purchase_id, request_options=request_options
        )


class AsyncRawPurchasesClient:
    """
    Async raw-response client for AsyncPurchasesClient.
    """

    def __init__(self, client: AsyncPurchasesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create_purchase_v2(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        quantity: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseV2RequestLanguage] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[List[CreatePurchaseV2Response]]:
        data = await AsyncPurchasesClient.create_purchase_v2(
            self._client,
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def list_purchases(
        self,
        *,
        purchase_id: Optional[str] = SENTINEL,
        iccid: Optional[str] = SENTINEL,
        after_date: Optional[str] = SENTINEL,
        before_date: Optional[str] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        after_cursor: Optional[str] = SENTINEL,
        limit: Optional[float] = SENTINEL,
        after: Optional[float] = SENTINEL,
        before: Optional[float] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPurchasesResponse]:
        data = await AsyncPurchasesClient.list_purchases(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "purchase_id": purchase_id,
                        "iccid": iccid,
                        "after_date": after_date,
                        "before_date": before_date,
                        "email": email,
                        "reference_id": reference_id,
                        "after_cursor": after_cursor,
                        "limit": limit,
                        "after": after,
                        "before": before,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_purchase(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        network_brand: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        language: Optional[CreatePurchaseRequestLanguage] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePurchaseResponse]:
        data = await AsyncPurchasesClient.create_purchase(
            self._client,
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "email": email,
                        "reference_id": reference_id,
                        "network_brand": network_brand,
                        "email_brand": email_brand,
                        "language": language,
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: Optional[str] = SENTINEL,
        end_date: Optional[str] = SENTINEL,
        duration: Optional[float] = SENTINEL,
        email: Optional[str] = SENTINEL,
        reference_id: Optional[str] = SENTINEL,
        email_brand: Optional[str] = SENTINEL,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[TopUpEsimResponse]:
        data = await AsyncPurchasesClient.top_up_esim(
            self._client,
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_date": start_date,
                        "end_date": end_date,
                        "duration": duration,
                        "email": email,
                        "reference_id": reference_id,
                        "email_brand": email_brand,
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: Optional[float] = SENTINEL,
        end_time: Optional[float] = SENTINEL,
        idempotency_key: Optional[str] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditPurchaseResponse]:
        data = await AsyncPurchasesClient.edit_purchase(
            self._client,
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "start_time": start_time,
                        "end_time": end_time,
                        "idempotency_key": idempotency_key,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_purchase_consumption(
        self, purchase_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetPurchaseConsumptionResponse]:
        data = await AsyncPurchasesClient.get_purchase_consumption(
            self._client, purchase_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
