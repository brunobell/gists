from numbers import Integral
from typing import Sequence

from magic_points import Point


class Points:
    """This is a simple example of sequence protocol, which
    entails just the __len__ and __getitem__ magic methods.
    __getitem__ is all that's needed to support iteration.
    """

    def __init__(self, points: Sequence[Point]):
        self._points = points

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__class__(self._points[index])
        if isinstance(index, Integral):
            return self._points[index]
        raise TypeError(f"{self.__class__.__name__} indices must be integers")
