import unittest
from . import implementation

class Validator(unittest.TestCase):
    def test_precondition_throws_if_no_input(self):
        validator = implementation.Validator()
        with self.assertRaises(Exception):
            validator.precondition()

    def test_precondition_does_not_throw_if_true(self):
        validator = implementation.Validator()
        validator.precondition(True)

    def test_postcondition_throws_if_no_input(self):
        validator = implementation.Validator()
        with self.assertRaises(Exception):
            validator.postcondition()

    def test_postcondition_does_not_throw_if_true(self):
        validator = implementation.Validator()
        validator.postcondition(True)

if __name__ == '__main__':
    unittest.main()