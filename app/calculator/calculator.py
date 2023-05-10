"""
"""

from __future__ import annotations
from typing import Callable


class InvalidValueTypeException(Exception):
    """
    """

    def __init__(self, value: float) -> None:
        """
        """
        self.value = value

    def __str__(self) -> str:
        """
        """
        value = self.value
        value_type = type(value)

        return f'Type of value "{value}" is "{value_type}" but it should be "float".'


def validate_arguments(
    function: Callable[[Calculator, float, float], float]
) -> Callable[[Calculator, float, float], float]:
    """
    """

    def wrapper(calculator: Calculator, value_1: float, value_2: float) -> float:
        """
        """
        value_1_is_valid = isinstance(value_1, float) or isinstance(value_1, int)

        if not value_1_is_valid:
            raise InvalidValueTypeException(value_1)

        value_2_is_valid = isinstance(value_2, float) or isinstance(value_1, int)

        if not value_2_is_valid:
            raise InvalidValueTypeException(value_2)

        return function(calculator, value_1, value_2)

    return wrapper


class Calculator:
    """
    """

    @validate_arguments
    def add(self, value_1: float, value_2: float) -> float:
        """
        """
        return value_1 + value_2

    @validate_arguments
    def sub(self, value_1: float, value_2: float) -> float:
        """
        """
        return value_1 - value_2

    @validate_arguments
    def mult(self, value_1: float, value_2: float) -> float:
        """
        """
        return value_1 * value_2

    @validate_arguments
    def div(self, value_1: float, value_2: float) -> float:
        """
        """
        if value_2 == 0:
            raise ZeroDivisionError("Divison by 0 not allowed!")

        return value_1 / value_2

    @validate_arguments
    def expo(self, value_1: float, value_2: float) -> float:
        """
        """
        # if value_2 == 0:
        #     return 1

        return value_1 ** value_2


def main() -> None:
    """
    """
    calculator = Calculator()

    res = calculator.add(1, 3)
    print(res)

    res = calculator.sub(10, 3)
    print(res)

    res = calculator.mult(2, 3)
    print(res)

    res = calculator.div(10, 2)
    print(res)

    res = calculator.expo(2, 3)
    print(res)

    # UNCOMMENT LINES BELOW TO CHECK THE EXCEPTIONS

    # WRONG TYPE
    # calculator.add("1", "3")

    # DIVISON BY ZERO
    # calculator.div(10, 0)


if __name__ == "__main__":
    """
    """
    main()
