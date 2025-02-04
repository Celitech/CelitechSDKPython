from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import TokenOkResponse


class IframeService(BaseService):

    @cast_models
    def token(self) -> TokenOkResponse:
        """Generate a new token to be used in the iFrame

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: TokenOkResponse
        """

        serialized_request = (
            Serializer(f"{self.base_url}/iframe/token", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_scopes({})
        )

        response, _, _ = self.send_request(serialized_request)
        return TokenOkResponse._unmap(response)
