"""Test case for custom enum types."""

import unittest
from itertools import accumulate

from custom_enum import ConnectionStatus


class TestConnectionStatus(unittest.TestCase):

    def test_str_representation(self):
        for status in ConnectionStatus:
            self.assertEqual(str(status), f'{status.name}({status.value})')

    def test_equality(self):
        #Check if enum members equal its value
        for status in ConnectionStatus:
            self.assertEqual(status, status.value)

        #Check if enum members equal each other
        seen = list()
        self.assertTrue(
            all(status not in seen or seen.append(status)
                for status in ConnectionStatus))

    def test_order(self):
        statuses = list(ConnectionStatus)
        self.assertTrue(all(x < y for x, y in zip(statuses, statuses[1:])))

    def test_truthtiness(self):
        self.assertFalse(
            any(status for status in ConnectionStatus
                if status != ConnectionStatus.CONNECTED))
        self.assertTrue(ConnectionStatus.CONNECTED)


if __name__ == '__main__':
    unittest.main(verbosity=2)
