from numbers import Real


class Point:

    def __init__(self, x: Real):
        self.__x = x

    @property
    def x(self) -> Real:
        return self.__x

    def __repr__(self) -> str:
        return f'Point({self.x})'

    def __str__(self) -> str:
        return f'({self.x})'

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            if self.x == other.x:
                return True
            return False
        raise TypeError(f'Expected Real or Point type, got {type(other)}')

    def __hash__(self):
        return self.x ^ 1

    def __abs__(self):
        return Point(abs(self.x))

    def __pos__(self):
        return Point(self.x)

    def __neg__(self):
        return Point(0-self.x)

    def __invert__(self):
        return Point(~self.x)

    def __int__(self):
        return int(self.x)

    def __float__(self):
        return float(self.x)

    def __add__(self, sop):
        if isinstance(sop, Real):
            return Point(self.x + sop)
        if isinstance(sop, Point):
            return Point(self.x + sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __sub__(self, sop):
        if isinstance(sop, Real):
            return Point(self.x - sop)
        if isinstance(sop, Point):
            return Point(self.x - sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __mul__(self, sop):
        if isinstance(sop, Real):
            return Point(self.x * sop)
        if isinstance(sop, Point):
            return Point(self.x * sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __truediv__(self, sop):
        if isinstance(sop, Real):
            return Point(self.x / sop)
        if isinstance(sop, Point):
            return Point(self.x / sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __mod__(self, sop):
        if isinstance(sop, Real):
            return Point(self.x % sop)
        if isinstance(sop, Point):
            return Point(self.x % sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __divmod__(self, sop):
        if isinstance(sop, Real):
            return tuple(map(Point, divmod(self.x, sop)))
        if isinstance(sop, Point):
            return tuple(map(Point, divmod(self.x, sop.x)))

    def __lshift__(self, sop):
        if isinstance(self, Real):
            return Point(self.x << sop)
        if isinstance(self, Point):
            return Point(self.x << sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __rshift__(self, sop):
        if isinstance(self, Real):
            return Point(self.x >> sop)
        if isinstance(self, Point):
            return Point(self.x >> sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __bool__(self):
        if self.x == 0:
            return False
        return True

    def __pow__(self, sop):
        if isinstance(sop, Real):
            return Point(self.x ** sop)
        if isinstance(sop, Point):
            return Point(self.x ** sop.x)
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __iadd__(self, sop):
        return self.__add__(sop)

    def __isub__(self, sop):
        return self.__sub__(sop)

    def __imul__(self, sop):
        return self.__mul__(sop)

    def __itruediv__(self, sop):
        return self.__truediv__(sop)

    def __ipow__(self, sop):
        return self.__pow__(sop)

    def __imod__(self, sop):
        return self.__mod__(sop)

    def __ilshift__(self, sop):
        return self.__lshift__(sop)

    def __irshift__(self, sop):
        return self.__rshift__(sop)

    def __radd__(self, sop):
        return self.__add__(sop)

    def __rsub__(self, sop):
        return self.__sub__(sop)

    def __rmul__(self, sop):
        return self.__mul__(sop)

    def __rtruediv__(self, sop):
        return self.__truediv__(sop)

    def __rpow__(self, sop):
        return self.__pow__(sop)

    def __rmod__(self, sop):
        return self.__mod__(sop)

    def __rdivmod__(self, sop):
        return self.__divmod__(sop)

    def __rlshift__(self, sop):
        return self.__lshift__(sop)

    def __rrshipt__(self, sop):
        return self.__rshift__(sop)

    def __gt__(self, sop):
        if isinstance(sop, Real):
            if self.x > sop:
                return True
            return False
        if isinstance(sop, Point):
            if self.x > sop.x:
                return True
            return False
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

    def __ge__(self, sop):
        if isinstance(sop, Real):
            if self.x >= sop:
                return True
            return False
        if isinstance(sop, Point):
            if self >= sop:
                return True
            return False
        raise TypeError(f'Expected Real or Point type, got {sop.__class__.__name__}')

