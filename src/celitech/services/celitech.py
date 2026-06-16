from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    CreatePurchaseRequest,
    CreatePurchaseV2Request,
    EditPurchaseRequest,
    TopUpESimRequest,
)


class CelitechService(BaseService):
    """
    Service class for CelitechService operations.
    Provides methods to interact with CelitechService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._list_destinations_config: SdkConfig = {"environment": Environment.API}
        self._list_packages_config: SdkConfig = {"environment": Environment.API}
        self._create_purchase_v2_config: SdkConfig = {"environment": Environment.API}
        self._top_up_e_sim_config: SdkConfig = {"environment": Environment.API}
        self._edit_purchase_config: SdkConfig = {"environment": Environment.API}
        self._get_purchase_consumption_config: SdkConfig = {
            "environment": Environment.API
        }
        self._create_purchase_config: SdkConfig = {"environment": Environment.API}
        self._list_purchases_config: SdkConfig = {"environment": Environment.API}
        self._get_e_sim_device_config: SdkConfig = {"environment": Environment.API}
        self._get_e_sim_history_config: SdkConfig = {"environment": Environment.API}
        self._get_e_sim_config: SdkConfig = {"environment": Environment.API}
        self._generate_token_config: SdkConfig = {"environment": Environment.API}

    def set_list_destinations_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_destinations.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_destinations_config = config
        return self

    def set_list_packages_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_packages.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_packages_config = config
        return self

    def set_create_purchase_v2_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_purchase_v2.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_purchase_v2_config = config
        return self

    def set_top_up_e_sim_config(self, config: SdkConfig):
        """
        Sets method-level configuration for top_up_e_sim.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._top_up_e_sim_config = config
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

    def set_get_e_sim_device_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_e_sim_device.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_e_sim_device_config = config
        return self

    def set_get_e_sim_history_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_e_sim_history.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_e_sim_history_config = config
        return self

    def set_get_e_sim_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_e_sim.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_e_sim_config = config
        return self

    def set_generate_token_config(self, config: SdkConfig):
        """
        Sets method-level configuration for generate_token.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._generate_token_config = config
        return self

    @cast_models
    def list_destinations(self, *, request_config: Optional[SdkConfig] = None) -> Any:
        """List Destinations

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        resolved_config = self._get_resolved_config(
            self._list_destinations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/destinations",
                [],
                resolved_config,
            )
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def list_packages(
        self,
        destination: Union[str, None] = SENTINEL,
        start_date: Union[str, None] = SENTINEL,
        end_date: Union[str, None] = SENTINEL,
        after_cursor: Union[str, None] = SENTINEL,
        limit: Union[str, None] = SENTINEL,
        start_time: Union[str, None] = SENTINEL,
        end_time: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """List Packages

        :param destination: ISO representation of the package's destination. Supports both ISO2 (e.g., 'FR') and ISO3 (e.g., 'FRA') country codes., defaults to None
        :type destination: str, optional
        :param start_date: Start date of the package's validity in the format 'yyyy-MM-dd'. This date can be set to the current day or any day within the next 12 months., defaults to None
        :type start_date: str, optional
        :param end_date: End date of the package's validity in the format 'yyyy-MM-dd'. End date can be maximum 90 days after Start date., defaults to None
        :type end_date: str, optional
        :param after_cursor: To get the next batch of results, use this parameter. It tells the API where to start fetching data after the last item you received. It helps you avoid repeats and efficiently browse through large sets of data., defaults to None
        :type after_cursor: str, optional
        :param limit: Maximum number of packages to be returned in the response. The value must be greater than 0 and less than or equal to 160. If not provided, the default value is 20, defaults to None
        :type limit: str, optional
        :param start_time: Epoch value representing the start time of the package's validity. This timestamp can be set to the current time or any time within the next 12 months, defaults to None
        :type start_time: str, optional
        :param end_time: Epoch value representing the end time of the package's validity. End time can be maximum 90 days after Start time, defaults to None
        :type end_time: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).is_optional().is_nullable().validate(destination)
        Validator(str).is_optional().is_nullable().validate(start_date)
        Validator(str).is_optional().is_nullable().validate(end_date)
        Validator(str).is_optional().is_nullable().validate(after_cursor)
        Validator(str).is_optional().is_nullable().validate(limit)
        Validator(str).is_optional().is_nullable().validate(start_time)
        Validator(str).is_optional().is_nullable().validate(end_time)

        resolved_config = self._get_resolved_config(
            self._list_packages_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/packages",
                [],
                resolved_config,
            )
            .add_query("destination", destination, nullable=True)
            .add_query("startDate", start_date, nullable=True)
            .add_query("endDate", end_date, nullable=True)
            .add_query("afterCursor", after_cursor, nullable=True)
            .add_query("limit", limit, nullable=True)
            .add_query("startTime", start_time, nullable=True)
            .add_query("endTime", end_time, nullable=True)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def create_purchase_v2(
        self,
        request_body: CreatePurchaseV2Request,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseV2Request
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreatePurchaseV2Request).is_nullable().validate(request_body)

        resolved_config = self._get_resolved_config(
            self._create_purchase_v2_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases/v2",
                [],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def top_up_e_sim(
        self,
        request_body: TopUpESimRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint is used to top-up an existing eSIM with the previously associated destination by providing its ICCID and package details. To determine if an eSIM can be topped up, use the Get eSIM endpoint, which returns the `isTopUpAllowed` flag.

        :param request_body: The request body.
        :type request_body: TopUpESimRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(TopUpESimRequest).is_nullable().validate(request_body)

        resolved_config = self._get_resolved_config(
            self._top_up_e_sim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases/topup",
                [],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def edit_purchase(
        self,
        request_body: EditPurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint allows you to modify the validity dates of an existing purchase. **Behavior:** - If the purchase has **not yet been activated**, both the start and end dates can be updated. - If the purchase is **already active**, only the **end date** can be updated, while the **start date must remain unchanged** (and should be passed as originally set). - Updates must comply with the same pricing structure; the modification cannot alter the package size or change its duration category. The end date can be extended or shortened as long as it adheres to the same pricing category and does not exceed the allowed duration limits.

        :param request_body: The request body.
        :type request_body: EditPurchaseRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(EditPurchaseRequest).is_nullable().validate(request_body)

        resolved_config = self._get_resolved_config(
            self._edit_purchase_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases/edit",
                [],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_scopes(set())
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_purchase_consumption(
        self, purchase_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """This endpoint can be called for consumption notifications (e.g. every 1 hour or when the user clicks a button). It returns the data balance (consumption) of purchased packages.

        :param purchase_id: purchase_id
        :type purchase_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(purchase_id)

        resolved_config = self._get_resolved_config(
            self._get_purchase_consumption_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases/{{purchaseId}}/consumption",
                [],
                resolved_config,
            )
            .add_path("purchaseId", purchase_id)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def create_purchase(
        self,
        request_body: CreatePurchaseRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """This endpoint is used to purchase a new eSIM by providing the package details.

        :param request_body: The request body.
        :type request_body: CreatePurchaseRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreatePurchaseRequest).is_nullable().validate(request_body)

        resolved_config = self._get_resolved_config(
            self._create_purchase_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/purchases",
                [],
                resolved_config,
            )
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

    @cast_models
    def get_e_sim_device(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """Get eSIM Device

        :param iccid: iccid
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(iccid)

        resolved_config = self._get_resolved_config(
            self._get_e_sim_device_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/esim/{{iccid}}/device",
                [],
                resolved_config,
            )
            .add_path("iccid", iccid)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_e_sim_history(
        self, iccid: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """Get eSIM History

        :param iccid: iccid
        :type iccid: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(iccid)

        resolved_config = self._get_resolved_config(
            self._get_e_sim_history_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/esim/{{iccid}}/history",
                [],
                resolved_config,
            )
            .add_path("iccid", iccid)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_e_sim(
        self,
        iccid: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Get eSIM

        :param iccid: ID of the eSIM, defaults to None
        :type iccid: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).is_optional().is_nullable().validate(iccid)

        resolved_config = self._get_resolved_config(
            self._get_e_sim_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/esim",
                [],
                resolved_config,
            )
            .add_query("iccid", iccid, nullable=True)
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def generate_token(self, *, request_config: Optional[SdkConfig] = None) -> Any:
        """Generate a new token to be used in the iFrame

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        resolved_config = self._get_resolved_config(
            self._generate_token_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.API.url or Environment.DEFAULT.url}/iframe/token",
                [],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return response
