"""Hash map.

This module provide a class HashMap that has the following operation:
    - hash(value): hash a int to corresponding position in hash map.
    - put(key, value): put a (key, value) pair into hash map.
    - get(key): get the value of key in hash map.
    - remove(key): remove the (key, value) pair from the hash map.
"""


class MyHashMap:
    """An implementation of hash map."""
    _maxsize = 1000

    def __init__(self):
        """Initial an empty hash map."""
        self._map = [None for _ in range(MyHashMap._maxsize)]

    @classmethod
    def hash(cls, key: int) -> int:
        """Hash key into the position in hash map."""
        return key & cls._maxsize - 1

    def put(self, key: int, value: int) -> None:
        """Add (key, value) pair to hash map."""
        hash_value = MyHashMap.hash(key)
        hash_slot = self._map[hash_value]

        if hash_slot:
            pair = next((pair for pair in hash_slot if pair.key == key), None)

            if not pair:
                hash_slot.append(Pair(key, value))
            else:
                pair.value = value
        else:
            self._map[hash_value] = [Pair(key, value)]

    def get(self, key: int) -> int:
        hash_value = MyHashMap.hash(key)
        hash_slot = self._map[hash_value]

        if hash_slot:
            value = next((pair.value for pair in hash_slot if pair.key == key),
                         None)
            if value is not None:
                return value

        return -1

    def remove(self, key: int) -> None:
        hash_value = MyHashMap.hash(key)
        hash_slot = self._map[hash_value]

        if hash_slot:
            pair = next((pair for pair in hash_slot if pair.key == key), None)
            if pair and pair.key == key:
                hash_slot.remove(pair)
                if not hash_slot:
                    hash_slot = None


class Pair:
    """A (key, value) pair of MyHashMap."""
    __slots__ = ('_key', '_value')

    def __init__(self, key: int, value: int):
        """Initilize the key and value."""
        self._key = key
        self.value = value

    @property
    def key(self) -> int:
        return self._key

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        if value >= 0:
            self._value = value
        else:
            raise ValueError('Value of Node must >= 0.')

    def __equal__(self, other):
        if isinstance(other, Pair):
            return self.key == other.key and self.value == other.value
        else:
            return NotImplemented


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
