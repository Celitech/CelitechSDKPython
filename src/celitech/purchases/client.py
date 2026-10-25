from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import CelitechEnvironment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
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
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        language: CreatePurchaseV2RequestLanguage = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> List[CreatePurchaseV2Response]:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseV2Request
        :param idempotency_key: Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces., defaults to None
        :type idempotency_key: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: List[CreatePurchaseV2Response]
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._create_purchase_v2_config, request_config
        )

        request_body = CreatePurchaseV2Request(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **{
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
            },
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
            else (response if isinstance(response, list) else [])
        )

    @cast_models
    def list_purchases(
        self,
        *,
        purchase_id: str = SENTINEL,
        iccid: str = SENTINEL,
        after_date: str = SENTINEL,
        before_date: str = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        after: float = SENTINEL,
        before: float = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> ListPurchasesResponse:
        """This endpoint can be used to list all the successful purchases made between a given interval.

        :param purchase_id: ID of the purchase, defaults to None
        :type purchase_id: str, optional
        :param iccid: ID of the eSIM, defaults to None
        :type iccid: str, optional
        :param after_date: Start date of the interval for filtering purchases in the format 'yyyy-MM-dd', defaults to None
        :type after_date: str, optional
        :param before_date: End date of the interval for filtering purchases in the format 'yyyy-MM-dd', defaults to None
        :type before_date: str, optional
        :param email: Email associated to the purchase., defaults to None
        :type email: str, optional
        :param reference_id: The referenceId that was provided by the partner during the purchase or topup flow., defaults to None
        :type reference_id: str, optional
        :param after_cursor: To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data., defaults to None
        :type after_cursor: str, optional
        :param limit: Maximum number of purchases to be returned in the response. The value must be greater than 0 and less than or equal to 100. If not provided, the default value is 20, defaults to None
        :type limit: float, optional
        :param after: Epoch value representing the start of the time interval for filtering purchases, defaults to None
        :type after: float, optional
        :param before: Epoch value representing the end of the time interval for filtering purchases, defaults to None
        :type before: float, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListPurchasesResponse
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
            self._list_purchases_config, request_config
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
                else response
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
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        language: CreatePurchaseRequestLanguage = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> CreatePurchaseResponse:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseRequest
        :param idempotency_key: Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces., defaults to None
        :type idempotency_key: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: CreatePurchaseResponse
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._create_purchase_config, request_config
        )

        request_body = CreatePurchaseRequest(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **{
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
            },
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
                else response
            )
        )

    @cast_models
    def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        email_brand: str = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> TopUpEsimResponse:
        """This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.

        :param request_body: The request body.
        :type request_body: TopUpEsimRequest
        :param idempotency_key: Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces., defaults to None
        :type idempotency_key: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: TopUpEsimResponse
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._top_up_esim_config, request_config
        )

        request_body = TopUpEsimRequest(
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **{
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
            },
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
                else response
            )
        )

    @cast_models
    def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> EditPurchaseResponse:
        """This endpoint allows you to modify the validity dates of an existing purchase. **Behavior:** - If the purchase has **not yet been activated**, both the start and end dates can be updated. - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set). - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category. The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits.

        :param request_body: The request body.
        :type request_body: EditPurchaseRequest
        :param idempotency_key: Optional. A unique value (for example a UUID) that makes this request safe to retry. If a request with the same `Idempotency-Key` and the same body succeeds, repeating it returns the original response instead of performing the action again, and the response includes the header `Idempotent-Replayed: true`. Keys are scoped to your credentials and remembered for 3 days. Only successful (2xx) responses are remembered, so a request that failed can be retried with the same key. Reusing a key with a different request returns `422`; sending it while the original request is still being processed returns `409`. If the idempotency store is temporarily unavailable, the request is not processed and returns `503`; retry it. Must be 1 to 255 printable ASCII characters, without spaces., defaults to None
        :type idempotency_key: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: EditPurchaseResponse
        """

        Validator(str).is_optional().validate(idempotency_key, "idempotency_key")

        resolved_config = self._get_resolved_config(
            self._edit_purchase_config, request_config
        )

        request_body = EditPurchaseRequest(
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **{
                k: v
                for k, v in {"start_time": start_time, "end_time": end_time}.items()
                if v is not SENTINEL
            },
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
                else response
            )
        )

    @cast_models
    def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> GetPurchaseConsumptionResponse:
        """This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

        :param purchase_id: ID of the purchase
        :type purchase_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetPurchaseConsumptionResponse
        """

        Validator(str).validate(purchase_id, "purchase_id")

        resolved_config = self._get_resolved_config(
            self._get_purchase_consumption_config, request_config
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
                else response
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

    def create_purchase_v2(
        self,
        *,
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
        language: CreatePurchaseV2RequestLanguage = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[List[CreatePurchaseV2Response]]:
        data = self._client.create_purchase_v2(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def list_purchases(
        self,
        *,
        purchase_id: str = SENTINEL,
        iccid: str = SENTINEL,
        after_date: str = SENTINEL,
        before_date: str = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        after: float = SENTINEL,
        before: float = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[ListPurchasesResponse]:
        data = self._client.list_purchases(
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_purchase(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        language: CreatePurchaseRequestLanguage = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[CreatePurchaseResponse]:
        data = self._client.create_purchase(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        email_brand: str = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[TopUpEsimResponse]:
        data = self._client.top_up_esim(
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[EditPurchaseResponse]:
        data = self._client.edit_purchase(
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **{
                k: v
                for k, v in {
                    "start_time": start_time,
                    "end_time": end_time,
                    "idempotency_key": idempotency_key,
                }.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetPurchaseConsumptionResponse]:
        data = self._client.get_purchase_consumption(
            purchase_id, request_config=request_config
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPurchasesClient(PurchasesClient):
    """
    Async wrapper for PurchasesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawPurchasesClient":
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
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        language: CreatePurchaseV2RequestLanguage = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[List[CreatePurchaseV2Response]]:
        return to_async(super().create_purchase_v2)(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **{
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
            },
            request_config=request_config,
        )

    def list_purchases(
        self,
        *,
        purchase_id: str = SENTINEL,
        iccid: str = SENTINEL,
        after_date: str = SENTINEL,
        before_date: str = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        after: float = SENTINEL,
        before: float = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListPurchasesResponse]:
        return to_async(super().list_purchases)(
            **{
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
            },
            request_config=request_config,
        )

    def create_purchase(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        language: CreatePurchaseRequestLanguage = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[CreatePurchaseResponse]:
        return to_async(super().create_purchase)(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **{
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
            },
            request_config=request_config,
        )

    def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        email_brand: str = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[TopUpEsimResponse]:
        return to_async(super().top_up_esim)(
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **{
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
            },
            request_config=request_config,
        )

    def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[EditPurchaseResponse]:
        return to_async(super().edit_purchase)(
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **{
                k: v
                for k, v in {
                    "start_time": start_time,
                    "end_time": end_time,
                    "idempotency_key": idempotency_key,
                }.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )

    def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[GetPurchaseConsumptionResponse]:
        return to_async(super().get_purchase_consumption)(
            purchase_id, request_config=request_config
        )


class AsyncRawPurchasesClient:
    """
    Async raw-response client for AsyncPurchasesClient.
    """

    def __init__(self, client: AsyncPurchasesClient):
        self._client = client

    async def create_purchase_v2(
        self,
        *,
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
        language: CreatePurchaseV2RequestLanguage = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[List[CreatePurchaseV2Response]]:
        data = await self._client.create_purchase_v2(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            quantity=quantity,
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def list_purchases(
        self,
        *,
        purchase_id: str = SENTINEL,
        iccid: str = SENTINEL,
        after_date: str = SENTINEL,
        before_date: str = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        after_cursor: str = SENTINEL,
        limit: float = SENTINEL,
        after: float = SENTINEL,
        before: float = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[ListPurchasesResponse]:
        data = await self._client.list_purchases(
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_purchase(
        self,
        *,
        destination: str,
        data_limit_in_gb: float,
        start_date: str,
        end_date: str,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        network_brand: str = SENTINEL,
        email_brand: str = SENTINEL,
        language: CreatePurchaseRequestLanguage = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[CreatePurchaseResponse]:
        data = await self._client.create_purchase(
            destination=destination,
            data_limit_in_gb=data_limit_in_gb,
            start_date=start_date,
            end_date=end_date,
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def top_up_esim(
        self,
        *,
        iccid: str,
        data_limit_in_gb: float,
        start_date: str = SENTINEL,
        end_date: str = SENTINEL,
        duration: float = SENTINEL,
        email: str = SENTINEL,
        reference_id: str = SENTINEL,
        email_brand: str = SENTINEL,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[TopUpEsimResponse]:
        data = await self._client.top_up_esim(
            iccid=iccid,
            data_limit_in_gb=data_limit_in_gb,
            **{
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
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def edit_purchase(
        self,
        *,
        purchase_id: str,
        start_date: str,
        end_date: str,
        start_time: float = SENTINEL,
        end_time: float = SENTINEL,
        idempotency_key: str = SENTINEL,
        request_config: Optional[SdkConfig] = None,
    ) -> HttpResponse[EditPurchaseResponse]:
        data = await self._client.edit_purchase(
            purchase_id=purchase_id,
            start_date=start_date,
            end_date=end_date,
            **{
                k: v
                for k, v in {
                    "start_time": start_time,
                    "end_time": end_time,
                    "idempotency_key": idempotency_key,
                }.items()
                if v is not SENTINEL
            },
            request_config=request_config,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> HttpResponse[GetPurchaseConsumptionResponse]:
        data = await self._client.get_purchase_consumption(
            purchase_id, request_config=request_config
        )
        return HttpResponse(data=data, response=self._client._last_response)
