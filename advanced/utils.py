
def get_user_number() -> float:
    """Ask the user for a valid number and return it.

    Returns:
        The number entered by the user is given back.
    """
    while True:
        try:
            number = float(input("Please enter a number: "))
            return number
        except ValueError:
            print("Invalid input. For the input to be valid please enter a number.")


def get_operation() -> str:
    """Ask the user for a valid calculator operation and return's it.

    Returns:
         This line is shown: The selected calculator operation (+, -, *, or /).
    """
    while True:
        operation = input("Chose one of the following operation's (+,-,*,/): ")

        if operation in ["+", "-", "*", "/"]:
            return operation
        else:
            print("This is an invalid operation. Please choose one of the following: +, -, *, /.")


