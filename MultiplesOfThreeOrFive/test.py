import unittest
from . import implementation

class TestMulitples(unittest.TestCase):

    def test_exsmple_case(self):
        multiples = implementation.Mulitples()
        self.assertEqual(multiples.multiples([3, 5], 10), 23)


if __name__ == '__main__':
    unittest.main()