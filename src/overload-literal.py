"""
TODO:

foo is a function that
returns an integer when second argument is 1,
returns a string when second argument is 2,
returns a list when second argument is 3,
otherwise it returns the first argument.
"""
from typing import Literal, overload, Any


@overload
def foo(value, flag: Literal[1]) -> int:
    ...


@overload
def foo(value, flag: Literal[2]) -> str:
    ...


@overload
def foo(value, flag: Literal[3]) -> list:
    ...


@overload
def foo[T](value: T, flag) -> T:
    ...


def foo(value, flag) -> Any:
    ...


foo("42", 1).bit_length()
foo(42, 2).upper()
foo(True, 3).append(1)
foo({}, "4").keys()

foo("42", 1).upper()  # type: ignore
foo(42, 2).append(1)  # type: ignore
foo(True, 3).bit_length()  # type: ignore
foo({}, "4").upper()  # type: ignore
