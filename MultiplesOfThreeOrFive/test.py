import unittest
from . import implementation

class TestMulitples(unittest.TestCase):

    def test_exsmple_case(self):
        multiples = implementation.Mulitples()
        self.assertEqual(multiples.multiples([3, 5], 10), 23)

    def test_raises_exception_when_factors_is_not_a_list(self):
        multiples = implementation.Mulitples()
        with self.assertRaises(Exception):
            multiples.multiples(3, 10)

    def test_raises_exception_when_factors_are_not_integers(self):
        multiples = implementation.Mulitples()
        with self.assertRaises(Exception):
            multiples.multiples([3.4, 7], 10)

    def test_raises_exception_when_factors_are_not_positive(self):
        multiples = implementation.Mulitples()
        with self.assertRaises(Exception):
            multiples.multiples([-3, 7], 10)


if __name__ == '__main__':
    unittest.main()