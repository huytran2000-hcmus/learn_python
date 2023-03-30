"""Custom sequence types.

This module provide my custom sequence types.
Classes:

    Fibonacci
"""
from decimal import Decimal
from functools import lru_cache


class Fibonacci:
    """Represent the Fibonacci sequence."""
    _cache_size = 2**8

    def __init__(self, n: int = 10) -> None:
        """Initialize a Fibonacci sequence upto Fn element(zeros-based)"""
        self.n = n

    @lru_cache(_cache_size)
    def _fib(self, n):
        """Return the Fn element(zero-based) in the Fibonacci sequence.
        
        LRU cache upto _cache_size results of the function.
        """
        if n == 0:
            return 0

        if n == 1:
            return 1

        return self._fib(n - 1) + self._fib(n - 2)

    @property
    def n(self) -> int:
        """Fibonacci sequence size(zero-based).
        
        It's must be posible to convert the assigned value to an integer.
        """
        return self._n

    @n.setter
    def n(self, n) -> None:
        try:
            n = int(n)
        except (ValueError, TypeError) as err:
            raise ValueError("n can't be convert to integer.") from err

        if n < 0:
            raise ValueError(
                f'Fibonacci: F(n) = F(n-1) + F(n-2) with n >= 0 but n = {n}')
        self._n = n

    def __len__(self):
        return self.n + 1

    def __getitem__(self, index) -> int:
        if isinstance(index, int):
            if index < 0:
                # Make index become positive
                index = index + len(self)

            if index < 0 or index >= len(self):
                raise IndexError(f'F({index}) is out of range')

            return self._fib(index)
        else:
            indices = index.indices(len(self))
            return [self._fib(idx) for idx in range(*indices)]

    def __repr__(self) -> str:
        return f'Fibonacci({self.n})'
