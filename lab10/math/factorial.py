import inspect


def factorial(number):
    """
    Recursive function that calculates the factorial of the given number.

    :return a number (factorial)
    """
    if not isinstance(number, int):
        raise Exception('Enter an integer number to find the factorial')
    if number == 1 or number == 2:
        return 1
    else:
        return number * factorial(number - 1)


def get_code():
    """
    :return the code for the factorial function
    """
    return inspect.getsource(factorial)
