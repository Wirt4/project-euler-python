import unittest
from even_fibonacci import Fibonacci

class TestEvenFibonacci(unittest.TestCase):
    def test_throws_if_bad_input(self):
        fibonacci = Fibonacci()
        with self.assertRaises(Exception):
            fibonacci.get_even_sum(-1)

    def test_does_not_throw_if_correct_input(self):
        fibonacci = Fibonacci()
        fibonacci.get_even_sum(1)

if __name__ == '__main__':
    unittest.main()