"""Module providing an example of function docstream"""


def add(num_a: int, num_b: int) -> int:
    """Simple Example Using autogen AutoDocStream Generator

    Args:
        num_a (int): num A
        num_b (int): num B

    Returns:
        int: add A + B
    """
    return num_a + num_b


def rest(num_a: int, num_b: int) -> int:
    """Simple Example Using autogen AutoDocStream Generator

    Args:
        num_a (int): num A
        num_b (int): num B

    Returns:
        int: add A - B
    """
    return num_a - num_b


help(add)
print(add(10, 20))
print(add.__doc__)
help(rest)
print(rest(10, 20))
print(rest.__doc__)


print(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")  # noqa: E501
