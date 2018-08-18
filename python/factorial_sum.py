"""A simple wrapper to calculate factorial sum from of a range."""


def factorial(n: 'int >= 0', history={}) -> int:
    if n < 0:
        raise ValueError(f"Non-negative expected, got {n}")
    if n == 0 or n == 1:
        fact = 1
    else:
        fact = n * factorial(n - 1)
    if n not in history:
        history[n] = fact
    return fact


def sum_of_factorials(n: 'int >= 0', start: 'int >= 0' = 0) -> int:
    return sum(map(factorial, range(min(n, start), max(n, start) + 1)))
