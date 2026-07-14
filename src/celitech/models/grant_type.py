from __future__ import annotations
from enum import Enum
from typing import Any


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
