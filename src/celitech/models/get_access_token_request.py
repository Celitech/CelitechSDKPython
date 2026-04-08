from enum import Enum
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class GrantType(str, Enum):
    """An enumeration representing different categories.

    :cvar CLIENTCREDENTIALS: "client_credentials"
    :vartype CLIENTCREDENTIALS: str
    """

    CLIENTCREDENTIALS = "client_credentials"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GrantType._member_map_.values()))


class GetAccessTokenRequest(BaseModel):
    """GetAccessTokenRequest

    :param grant_type: grant_type, defaults to None
    :type grant_type: GrantType, optional
    :param client_id: client_id, defaults to None
    :type client_id: str, optional
    :param client_secret: client_secret, defaults to None
    :type client_secret: str, optional
    """

    grant_type: Optional[GrantType] = Field(default=None)
    client_id: Optional[str] = Field(default=None)
    client_secret: Optional[str] = Field(default=None)
