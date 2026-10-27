from typing import cast


def add(number_1: float, number_2: float) -> float:
    """Add two numbers together and return the sum.

    Parameters:
        number_1: The first number.
        number_2: The second number.

    Returns:
        The sum of the two numbers together.
    """
    return number_1 + number_2


def subtract(number_1: float, number_2: float) -> float:
    """Subtract the second number from the first number for the result.
        Parameters:
            number_1: The first number.
            number_2: The second number.

        Returns:
            The difference between the two numbers.
        """
    return number_1 - number_2


def multiply(number_1: float, number_2: float) -> float:
    """Multiply the two numbers together and return their product.
    Parameters:
        number_1: The first number
        number_2: The second number.
    Returns:
        The product of the two numbers gets you the result.
     """
    return number_1 * number_2


def divide(number_1: float, number_2: float) -> float:
    """Divide the first number by the second one.
    Parameters:
        number_1:  The first number
        number_2: The second number.
    Returns: The division of these two numbers give you the quotient.
    """

    return number_1 / number_2
