from numbers import Integral
from typing import Sequence

from magic_points import Point


class Points:
    """This is a simple example of sequence protocol, which
    entails just the __len__ and __getitem__ magic methods.
    __getitem__ is all that's needed to support iteration.

    >>> points = Points([Point(x) for x in range(10)]); print(len(points))
    10
    >>> points[0]
    Point(0)
    >>> points[5]
    Point(5)
    >>> points[2:5]
    Points([Point(2), Point(3), Point(4)])
    """

    def __init__(self, points: Sequence[Point]):
        self._points = points

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__class__(self._points[index])
        if isinstance(index, Integral):
            return self._points[index]
        raise TypeError(f"{self.__class__.__name__} indices must be integers")

    def __len__(self):
        return len(self._points)

    def __repr__(self):
        return f'Points({self._points})'

    def __str__(self):
        return ', '.join([str(point) for point in self._points]).join('[]')
