import unittest

from largest_prime_factor import PrimeFactors

class TestLargestPrimeFactor(unittest.TestCase):

    def test_precondition(self):
        primes = PrimeFactors()
        with self.assertRaises(Exception):
            primes.largest_prime_factor(1.5)


if __name__ == '__main__':
    unittest.main()