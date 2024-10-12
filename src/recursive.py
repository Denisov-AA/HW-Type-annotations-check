"""
TODO:

Define a `Tree` type. `Tree` is a dictionary, whose keys are string, values are also `Tree`.
"""
from typing import Dict, TypeAlias
type Tree = Dict[str, "Tree"]


def f(t: Tree):
    pass


f({})
f({"foo": {}})
f({"foo": {"bar": {}}})
f({"foo": {"bar": {"baz": {}}}})

f(1)  # type: ignore
f({"foo": []})  # type: ignore
f({"foo": {1: {}}})  # type: ignore
