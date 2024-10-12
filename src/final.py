"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""
from typing import List, Final

my_list: Final[List[int]] = []

my_list.append(1)
my_list = []  # type: ignore
my_list = "something else"  # type: ignore