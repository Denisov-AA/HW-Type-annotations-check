"""
TODO:

foo should accept a argument that's either a string or integer.
"""
from typing import Union


def foo(x: Union[str, int]):
    pass


foo("foo")
foo(1)

foo([])  # expect-type-error
