import re
from typing import Union, Any, Type, Pattern, get_args
from ...models.base import OneOfBaseModel


class Validator:
    """
    A simple validator class for validating the type and pattern of a value.

    :ivar Type[Any] _type: The expected type for the value.
    :ivar bool _is_optional: Flag indicating whether the value is optional.
    :ivar bool _is_array: Flag indicating whether the value is an array.
    :ivar Pattern[str] _pattern: The regular expression pattern for validating the value.
    :ivar int _min: The minimum value for validating the value.
    :ivar int _max: The maximum value for validating the value.
    """

    def __init__(self, _type: Type[Any] = None):
        """
        Initializes a Validator instance.

        :param Type[Any] _type: The expected type for the value. Defaults to None.
        """
        self._type: Type[Any] = _type
        self._is_optional: bool = False
        self._is_array: bool = False
        self._pattern: Pattern[str] = None
        self._min: int = None
        self._max: int = None

    def is_array(self) -> "Validator":
        """
        Marks the value as an array.

        :return: The Validator instance for method chaining.
        :rtype: Validator
        """
        self._is_array = True
        return self

    def is_optional(self) -> "Validator":
        """
        Marks the value as optional.

        :return: The Validator instance for method chaining.
        :rtype: Validator
        """
        self._is_optional = True
        return self

    def pattern(self, pattern: str) -> "Validator":
        """
        Specifies a regular expression pattern for validating the value.

        :param str pattern: The regular expression pattern.
        :return: The Validator instance for method chaining.
        :rtype: Validator
        """
        self._pattern = re.compile(pattern)
        return self

    def min(self, min: int) -> "Validator":
        """
        Specifies a minimum value for validating the value.

        :param int min: The minimum value.
        :return: The Validator instance for method chaining.
        :rtype: Validator
        """
        self._min = min
        return self

    def max(self, max: int) -> "Validator":
        """
        Specifies a maximum value for validating the value.

        :param int max: The maximum value.
        :return: The Validator instance for method chaining.
        :rtype: Validator
        """
        self._max = max
        return self

    def validate(self, value: Any) -> None:
        """
        Validates the provided value based on the specified criteria.

        :param Any value: The input that needs to be checked
        :raises ValueError: If the value does not meet the specified validation criteria.
        """
        if not self._type:
            raise TypeError("Invalid type: No type specified")
        if self._is_optional and value is None:
            return

        self._validate_type(value)
        self._validate_rules(value)

    def _validate_type(self, value: Any) -> None:
        """
        Validates the type of the value.

        :param Any value: The input that needs to be checked
        :raises ValueError: If the value does not meet the expected type.
        """
        if self._is_one_of_type(self._type):
            self._validate_one_of_type(value)
        elif self._is_array:
            self._validate_array_type(value)
        elif not self._match_type(value):
            raise TypeError(f"Invalid type: Expected {self._type}, got {type(value)}")

    def _validate_one_of_type(self, value: Any) -> None:
        """
        Validates oneOf model type.

        :param Any value: The input that needs to be checked
        :raises ValueError: If the value does not match the oneOf rules.
        """
        class_list = {arg.__name__: arg for arg in get_args(self._type) if arg.__name__}
        OneOfBaseModel.class_list = class_list
        OneOfBaseModel.return_one_of(value)

    def _validate_array_type(self, value: Any) -> None:
        """
        Validates the type of an array value.

        :param Any value: The input that needs to be checked
        :raises ValueError: If the array items do not match the expected type.
        """
        if any(self._match_type(v) is False for v in value):
            raise TypeError(f"Invalid type: Expected {self._type}, got {type(value)}")

    def _match_type(self, value: Any) -> bool:
        """
        Checks if the value matches the expected type.

        :param Any value: The input that needs to be checked
        :raises ValueError: If the value does not match the expected type.
        """
        is_numeric = self._type is float and isinstance(value, int)
        if isinstance(value, self._type) or is_numeric:
            return True
        return False

    def _validate_rules(self, value: Any) -> None:
        """
        Validate the rules specified for the value.

        :param Any value: The input that needs to be validated
        :raises ValueError: If the value does not meet the specified validation criteria.
        """
        if self._min is not None and value < self._min:
            raise ValueError(f"Invalid value: {value} is less than {self._min}")
        if self._max is not None and value > self._max:
            raise ValueError(f"Invalid value: {value} is greater than {self._max}")
        if self._pattern and not self._pattern.match(str(value)):
            raise ValueError(
                f"Invalid value: {value} does not match pattern {self._pattern}"
            )

    def _is_one_of_type(self, cls_type):
        """
        Checks if the provided type is a Union type.

        :param Type[Any] cls_type: The type to be checked.
        :return: True if the type is a Union type, False otherwise.
        :rtype: bool
        """
        return hasattr(cls_type, "__origin__") and cls_type.__origin__ is Union
