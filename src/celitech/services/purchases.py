from typing import Any, Optional, List, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    BadRequest,
    CreatePurchaseOkResponse,
    CreatePurchaseRequest,
    CreatePurchaseV2OkResponse,
    CreatePurchaseV2Request,
    EditPurchaseOkResponse,
    EditPurchaseRequest,
    GetPurchaseConsumptionOkResponse,
    ListPurchasesOkResponse,
    TopUpEsimOkResponse,
    TopUpEsimRequest,
    Unauthorized,
)


class PurchasesService(BaseService):
    """
    Service class for PurchasesService operations.
    Provides methods to interact with PurchasesService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
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

    @cast_models
    def create_purchase_v2(
        self,
        request_body: CreatePurchaseV2Request,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> List[CreatePurchaseV2OkResponse]:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseV2Request
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: List[CreatePurchaseV2OkResponse]
        """

        Validator(CreatePurchaseV2Request).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._create_purchase_v2_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/purchases/v2",
                [],
                resolved_config,
            )
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return [CreatePurchaseV2OkResponse.model_validate(item) for item in response]

    @cast_models
    def list_purchases(
        self,
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
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> ListPurchasesOkResponse:
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
        :rtype: ListPurchasesOkResponse
        """

        Validator(str).is_optional().validate(purchase_id)
        Validator(str).is_optional().min_length(18).max_length(22).validate(iccid)
        Validator(str).is_optional().validate(after_date)
        Validator(str).is_optional().validate(before_date)
        Validator(str).is_optional().validate(email)
        Validator(str).is_optional().validate(reference_id)
        Validator(str).is_optional().validate(after_cursor)
        Validator(float).is_optional().validate(limit)
        Validator(float).is_optional().validate(after)
        Validator(float).is_optional().validate(before)

        resolved_config = self._get_resolved_config(
            self._list_purchases_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/purchases",
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
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return ListPurchasesOkResponse.model_validate(response)

    @cast_models
    def create_purchase(
        self,
        request_body: CreatePurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> CreatePurchaseOkResponse:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: CreatePurchaseOkResponse
        """

        Validator(CreatePurchaseRequest).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._create_purchase_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/purchases",
                [],
                resolved_config,
            )
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return CreatePurchaseOkResponse.model_validate(response)

    @cast_models
    def top_up_esim(
        self,
        request_body: TopUpEsimRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> TopUpEsimOkResponse:
        """This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.

        :param request_body: The request body.
        :type request_body: TopUpEsimRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: TopUpEsimOkResponse
        """

        Validator(TopUpEsimRequest).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._top_up_esim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/purchases/topup",
                [],
                resolved_config,
            )
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return TopUpEsimOkResponse.model_validate(response)

    @cast_models
    def edit_purchase(
        self,
        request_body: EditPurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> EditPurchaseOkResponse:
        """This endpoint allows you to modify the validity dates of an existing purchase. **Behavior:** - If the purchase has **not yet been activated**, both the start and end dates can be updated. - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set). - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category. The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits.

        :param request_body: The request body.
        :type request_body: EditPurchaseRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: EditPurchaseOkResponse
        """

        Validator(EditPurchaseRequest).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._edit_purchase_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/purchases/edit",
                [],
                resolved_config,
            )
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return EditPurchaseOkResponse.model_validate(response)

    @cast_models
    def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> GetPurchaseConsumptionOkResponse:
        """This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

        :param purchase_id: ID of the purchase
        :type purchase_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: GetPurchaseConsumptionOkResponse
        """

        Validator(str).validate(purchase_id)

        resolved_config = self._get_resolved_config(
            self._get_purchase_consumption_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/purchases/{{purchaseId}}/consumption",
                [],
                resolved_config,
            )
            .add_path("purchaseId", purchase_id)
            .add_error(400, BadRequest)
            .add_error(401, Unauthorized)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, status, _ = self.send_request(serialized_request)
        return GetPurchaseConsumptionOkResponse.model_validate(response)
