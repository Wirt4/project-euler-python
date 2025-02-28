import unittest
from . import implementation

class TestEvenFibonacci(unittest.TestCase):
    def test_throws_if_bad_input(self):

        fibonacci = implementation.Fibonacci()
        with self.assertRaises(Exception):
            fibonacci.get_even_sum(-1)

if __name__ == '__main__':
    unittest.main()