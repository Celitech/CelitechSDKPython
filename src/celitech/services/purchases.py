from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import CreatePurchaseRequest


class PurchasesService(BaseService):
    """
    Service class for PurchasesService operations.
    Provides methods to interact with PurchasesService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._create_purchase_config: SdkConfig = {"environment": Environment.API}
        self._list_purchases_config: SdkConfig = {"environment": Environment.API}

    def set_create_purchase_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_purchase.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_purchase_config = config
        return self

    def set_list_purchases_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_purchases.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_purchases_config = config
        return self

    @cast_models
    def create_purchase(
        self,
        request_body: CreatePurchaseRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseRequest
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreatePurchaseRequest).is_nullable().validate(request_body)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._create_purchase_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def list_purchases(
        self,
        accept: Union[str, None],
        purchase_id: Union[str, None] = SENTINEL,
        iccid: Union[str, None] = SENTINEL,
        after_date: Union[str, None] = SENTINEL,
        before_date: Union[str, None] = SENTINEL,
        email: Union[str, None] = SENTINEL,
        reference_id: Union[str, None] = SENTINEL,
        after_cursor: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        after: Union[str, None] = SENTINEL,
        before: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint can be used to list all the successful purchases made between a given interval.

        :param accept: accept
        :type accept: str
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
        :type limit: str, optional
        :param after: Epoch value representing the start of the time interval for filtering purchases, defaults to None
        :type after: str, optional
        :param before: Epoch value representing the end of the time interval for filtering purchases, defaults to None
        :type before: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).is_nullable().validate(accept)
        Validator(str).is_optional().is_nullable().validate(purchase_id)
        Validator(str).is_optional().is_nullable().validate(iccid)
        Validator(str).is_optional().is_nullable().validate(after_date)
        Validator(str).is_optional().is_nullable().validate(before_date)
        Validator(str).is_optional().is_nullable().validate(email)
        Validator(str).is_optional().is_nullable().validate(reference_id)
        Validator(str).is_optional().is_nullable().validate(after_cursor)
        Validator(str).is_optional().is_nullable().validate(limit)
        Validator(str).is_optional().is_nullable().validate(after)
        Validator(str).is_optional().is_nullable().validate(before)

        resolved_config = self._get_resolved_config(
            self._list_purchases_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases",
                [],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_query("purchaseId", purchase_id, nullable=True)
            .add_query("iccid", iccid, nullable=True)
            .add_query("afterDate", after_date, nullable=True)
            .add_query("beforeDate", before_date, nullable=True)
            .add_query("email", email, nullable=True)
            .add_query("referenceId", reference_id, nullable=True)
            .add_query("afterCursor", after_cursor, nullable=True)
            .add_query("limit", limit, nullable=True)
            .add_query("after", after, nullable=True)
            .add_query("before", before, nullable=True)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
