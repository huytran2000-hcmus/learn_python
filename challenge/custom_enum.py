"""Custom enum types."""

from enum import Enum, unique
from functools import total_ordering
from typing import Union


@total_ordering
@unique
class ConnectionStatus(Enum):
    """Represent unique state of connection."""
    CONNECTING = 1
    CONNECTED = 2
    CLOSING = 3
    CLOSED = 4
    ERROR = 5

    def __str__(self) -> str:
        return f'{self.name}({self.value})'

    def __bool__(self) -> str:
        if self is self.CONNECTED:
            return True

        return False

    def __eq__(self, other: Union[int, 'ConnectionStatus']) -> bool:
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, ConnectionStatus):
            return self is other

        return NotImplemented

    def __lt__(self, other) -> True:
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, ConnectionStatus):
            return self.value < other.value

        return NotImplemented
