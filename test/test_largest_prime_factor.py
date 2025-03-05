import unittest

from largest_prime_factor import PrimeFactors

class TestLargestPrimeFactor(unittest.TestCase):

    def test_precondition(self):
        primes = PrimeFactors()
        with self.assertRaises(Exception):
            primes.largest_prime_factor(1.5)

    def test_small_example(self):
        primes = PrimeFactors()
        self.assertEqual(primes.largest_prime_factor(13195), 29)

    def test_paper_draft_example(self):
        primes = PrimeFactors()
        self.assertEqual(primes.largest_prime_factor(27), 3)

    def test_question_example(self):
        primes = PrimeFactors()
        self.assertEqual(primes.largest_prime_factor(600851475143), 6857)



if __name__ == '__main__':
    unittest.main()