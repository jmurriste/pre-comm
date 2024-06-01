from __future__ import annotations  # no required

from dataclasses import dataclass
from typing import (
    Generic,
    List,
    NamedTuple,
    TypedDict,
    TypeVar,
    Union,
)


class Point(NamedTuple):
    x: int
    y: int


class Student3(TypedDict):
    name: str
    age: int
    position: Point
    friends: List[Student3]


TStudentArgsDict = Union[str, int, Point, List[Student3]]

TAddableEntity = TypeVar(
    "TAddableEntity", int, float, str, list, tuple
)  # generic type var


def add(a: TAddableEntity, b: TAddableEntity) -> List[TAddableEntity]:
    """_summary_

    Args:
        a (TAddableEntity): _description_
        b (TAddableEntity): _description_

    Returns:
        TAddableEntity: _description_
    """
    return [a + b]


print(add("int", "noint"))
# print(add("int", int(1)))


TException = TypeVar("TException", bound=Exception)


def raise_exception(err: TException) -> TException:
    raise err


raise_exception(ValueError("value error not correct"))


# to similate hieritance we can create class and subclases using generics and
# bounds classes toghether.

TFriend = TypeVar("TFriend")
TFriend_2 = TypeVar("TFriend_2")

TFriend_3 = TypeVar("TFriend_3", "Animal", "Student")


@dataclass
class Animal: ...


TFriend_4 = TypeVar("TFriend_4", Animal, "Student")


@dataclass
class Student(Generic[TFriend, TFriend_2]):
    name: str
    age: int
    position: Point
    friends: List[TFriend]
    friends_2: List[TFriend_2]


students_that_only_likes_animas: Student[Animal, int] = Student(
    name="pepe",
    age=30,
    position=Point(1, 2),
    friends=[Animal()],
    friends_2=[1],
)
