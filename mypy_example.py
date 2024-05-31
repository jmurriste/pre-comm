from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

var: int = 1
var = "jorge"

abc: Any = "Pepe"
lista: list[int] = [1, 2, 3, 4]  # python 3.9+
Lista: List[int] = [1, 2, 3, 4]  # python -3.9, needs import statement
three_dim_vetor: tuple[int, int, str] = (1, 1, "Jorge")
three_dim_vetor_T: Tuple[int, int, str] = (1, 1, "Jorge")
student_to_ages: dict[str, int] = {"bobby": 11, "pedro": 15, "mama": 20}
fruits: set[str] = {"apple", "kiwi"}
misc_values: List[Union[int, float, str, type]] = [1, 1.0, "Jorge", object]  # could be any of those types.
x: int | float | str
x = 1
x = 1.2
x = "jorge"
ab: Optional[int] = 1  # or can be None


def greet(name: str | None = None):
    """greeting by name

    Args:
        name (str | None, optional): name. Defaults to None.
    """
    if not name:
        print("Hello")
        return
    else:
        print(f"Hello {name}")
        return


greet()
greet("jorge")


def greet2(name: Optional[str] = None):
    """greeting by name

    Args:
        name (str | None, optional): name. Defaults to None.
    """
    if not name:
        print("Hello")
        return
    else:
        print(f"Hello {name}")
        return

greet2()
greet2("martin")
