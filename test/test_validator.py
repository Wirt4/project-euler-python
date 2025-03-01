import unittest
from validator import Validator

class TestValidator(unittest.TestCase):
    def test_precondition_throws_if_no_input(self):
        v = Validator()
        with self.assertRaises(Exception):
            v.precondition()

    def test_precondition_does_not_throw_if_true(self):
        v = Validator()
        v.precondition(True)

    def test_postcondition_throws_if_no_input(self):
        v = Validator()
        with self.assertRaises(Exception):
            v.postcondition()

    def test_postcondition_does_not_throw_if_true(self):
        v = Validator()
        v.postcondition(True)

if __name__ == '__main__':
    unittest.main()