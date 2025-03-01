import unittest
from multiples_of_three_or_five import Multiples

class TestMultiples(unittest.TestCase):
  
    def test_example_case(self):
        multiples = Multiples()
        self.assertEqual(multiples.multiples([3, 5], 10), 23)

    def test_small_extention(self):
        multiples = Multiples()
        self.assertEqual(multiples.multiples([3, 5], 12), 33)

    def test_raises_exception_when_factors_is_not_a_list(self):
        multiples = Multiples()
        with self.assertRaises(Exception):
            multiples.multiples(3, 10)

    def test_raises_exception_when_factors_are_not_integers(self):
        multiples = Multiples()
        with self.assertRaises(Exception):
            multiples.multiples([3.4, 7], 10)

    def test_raises_exception_when_factors_are_not_positive(self):
        multiples = Multiples()
        with self.assertRaises(Exception):
            multiples.multiples([-3, 7], 10)

    def test_raises_exception_when_limit_is_not_a_positive_integer(self):
        multiples = Multiples()
        with self.assertRaises(Exception):
            multiples.multiples([3, 7], -10)

    def test_raises_exception_when_is_zero_is_passed(self):
        multiples = Multiples()
        with self.assertRaises(Exception):
            multiples.multiples([3, 7], 0)

    def test_answer_case(self):
        multiples = Multiples()
        self.assertEqual(multiples.multiples([3, 5], 1000), 233168)


if __name__ == '__main__':
    unittest.main()