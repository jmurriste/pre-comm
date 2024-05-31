from __future__ import annotations  # no required

from dataclasses import dataclass
from typing import (
    Any,
    List,
    NamedTuple,
    Optional,
    Tuple,
    TypedDict,
    Union,
)


class Point(NamedTuple):
    x: int
    y: int


point = Point(x=1, y=2)
print(point)
print(point.x)
print(point.y)


class Student:

    def __init__(
        self,
        name: str,
        age: int,
        position: Point,
        friends: List["Student"],
    ) -> None:
        self.name: str = name
        self.age: int = age
        self.position: Point = position
        self.friends = friends


student = Student(name="Jorge", age=33, position=Point(1, 2), friends=[])
print(student)


@dataclass
class Student2:
    name: str
    age: int
    position: Point
    friends: List[Student2]


strudent2 = Student2(
    **{
        "name": "jorge",
        "age": 33,
        "position": Point(1, 2),
        "friends": [
            {
                "name": "pepe",
                "age": 33,
                "position": Point(2, 4),
                "friends": [],
            }
        ],
    }
)
print(strudent2)
print(strudent2.name)
print(strudent2.friends[0]["name"])


class Student3(TypedDict):
    name: str
    age: int
    position: Point
    friends: List[Student3]


strudent3: Student3 = {
    "name": "jorge",
    "age": 33,
    "position": Point(1, 2),
    "friends": [
        {
            "name": "pepe",
            "age": 33,
            "position": Point(2, 4),
            "friends": [],
        }
    ],
}
print(strudent3)
