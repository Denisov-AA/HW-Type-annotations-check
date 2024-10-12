"""
TODO:

`make_object` takes a class returns an instance of it.
"""
from typing import Any


def make_object(cls: type[Any]):
    return cls()


class MyClass:
    pass


def f():
    pass


c = make_object(MyClass)
c = make_object(int)
c = make_object(f)  # type: ignore
c = make_object("sss")  # type: ignore
c = make_object(["sss"])  # type: ignore
