"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""
from typing import Dict


def foo_2(x: Dict[str, str]):
    pass


foo_2({"foo": "bar"})
foo_2({"foo": 1})  # type: ignore