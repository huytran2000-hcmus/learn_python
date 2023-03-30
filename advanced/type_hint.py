'''Test type hint(type annotation)'''

from typing import Any


def say_hi(name: Any) -> str:
    '''Return a greeting base on your name.'''
    return f"Hi, my name{name}"


say_hi(1)
