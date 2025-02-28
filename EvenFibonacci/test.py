import unittest
from . import implementation

class TestEvenFibonacci(unittest.TestCase):
    def test_throws_if_bad_input(self):
        fibonacci = implementation.Fibonacci()
        with self.assertRaises(Exception):
            fibonacci.get_even_sum(-1)

    def test_does_not_throw_if_correct_input(self):
        fibonacci = implementation.Fibonacci()
        fibonacci.get_even_sum(1)

if __name__ == '__main__':
    unittest.main()