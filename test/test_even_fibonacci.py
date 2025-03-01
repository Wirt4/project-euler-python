import unittest
from even_fibonacci import Fibonacci

class TestEvenFibonacci(unittest.TestCase):
    def test_throws_if_bad_input(self):
        fibonacci = Fibonacci()
        with self.assertRaises(Exception):
            fibonacci.get_even_sum(-1)

    def test_base_case_1(self):
        self.assertEqual(Fibonacci().get_even_sum(1), 0)

    def test_base_case_2(self):
        self.assertEqual(Fibonacci().get_even_sum(10), 44)

if __name__ == '__main__':
    unittest.main()