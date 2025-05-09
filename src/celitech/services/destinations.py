from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import ListDestinationsOkResponse


class DestinationsService(BaseService):

    @cast_models
    def list_destinations(self) -> ListDestinationsOkResponse:
        """List Destinations

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListDestinationsOkResponse
        """

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/destinations",
            )
            .serialize()
            .set_method("GET")
            .set_scopes(set())
        )

        response, _, _ = self.send_request(serialized_request)
        return ListDestinationsOkResponse._unmap(response)
