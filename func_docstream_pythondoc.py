"""Module providing an example of function docstream"""


def calc(num_a: int, num_b: int) -> int:
    """Summary or Description of the Function

    Parameters:
    num_a (int): first number
    num_b (int): second number

    Returns:
    int:Returning value num_a + num_b

    """
    return num_a + num_b


def rest(num_a: int, num_b: int) -> int:
    """Returning a two number substraction"""
    return num_a - num_b


help(calc)
print(calc(10, 20))
print(calc.__doc__)
help(rest)
print(rest(10, 20))
print(rest.__doc__)


print(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
)  # noqa: E501
