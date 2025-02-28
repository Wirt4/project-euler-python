import unittest
from . import implementation

class Validator(unittest.TestCase):
    def test_precondition_throws_if_no_input(self):
        validator = implementation.Validator()
        with self.assertRaises(Exception):
            validator.precondition()

if __name__ == '__main__':
    unittest.main()