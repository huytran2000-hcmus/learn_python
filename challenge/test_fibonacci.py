import unittest

from custom_sequence_types import Fibonacci


class TestFibonacci(unittest.TestCase):
    """Test case for Fibonacci."""

    def test_n(self):
        """Test Fibonacci with illegal n."""
        with self.assertRaises(ValueError):
            fib = Fibonacci(None)
            fib = Fibonacci('s')
            fib = Fibonacci(-1)
            fib = Fibonacci(-3.1)
            fib = Fibonacci('-1')

    def test_indexed(self):
        """Test if Fibonacci instance return appropriate value."""
        fib = Fibonacci(20)

        #Indexing
        self.assertEqual(fib[0], 0)
        self.assertEqual(fib[1], 1)
        self.assertEqual(fib[2], 1)
        self.assertEqual(fib[5], 5)
        self.assertEqual(fib[10], 55)
        self.assertEqual(fib[11], 89)
        self.assertEqual(fib[15], 610)
        self.assertEqual(fib[-1], 6765)
        self.assertEqual(fib[-len(fib)], 0)

        #Slicing
        F7to14 = [13, 21, 34, 55, 89, 144, 233, 377]
        self.assertEqual(fib[:], list(fib))
        self.assertEqual(fib[7:10], F7to14[0:3])
        self.assertEqual(fib[-10:14], F7to14[4:-1])

        #Slicing with step
        self.assertEqual(fib[::-1], list(reversed(fib)))
        self.assertEqual(fib[7:15:2], F7to14[::2])
        self.assertEqual(fib[14:6:-2], F7to14[::-2])

    def test_out_of_range(self):
        """Test Fibonacci instance with out of range indexes."""
        fib = Fibonacci(10)
        with self.assertRaises(IndexError):
            fib[len(fib)]
        with self.assertRaises(IndexError):
            fib[-len(fib) - 1]

    def test_cache(self):
        """Test if Fibonacci instance cache fibonacci elements."""
        cache_size = Fibonacci._cache_size
        fib = Fibonacci(cache_size + 3)
        size = 10
        inc_size = 3
        cache_size = Fibonacci._cache_size

        fib[size - 1]
        self.assertEqual(fib._fib.cache_info().currsize, size)

        size += inc_size
        fib[size - 1]
        self.assertEqual(fib._fib.cache_info().hits, size - (inc_size - 1))
        self.assertEqual(fib._fib.cache_info().currsize, size)

        fib[cache_size - 1]
        self.assertEqual(fib._fib.cache_info().hits, cache_size - 1)
        self.assertEqual(fib._fib.cache_info().currsize, cache_size)


if __name__ == '__main__':
    unittest.main(verbosity=2)
