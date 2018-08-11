"""Four different types of python decorator implementations."""


import functools


def decorator_without_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def decorator_with_args(*dargs, **dkwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


class DecoratorClassWithoutArgs:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class DecoratorClassWithArgs:
    def __init__(self, *dargs, **dkwargs):
        self.dargs = dargs
        self.dkwargs = dkwargs

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
