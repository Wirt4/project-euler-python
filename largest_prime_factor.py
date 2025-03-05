"""
The prime factors of 13195 are  5, 7 13, and 29.

What is the largest prime factor of the number 600851475143?
"""

from validator import Validator


class PrimeFactors:
    def __init__(self):
        self.v = Validator()
    
    def largest_prime_factor(self, n):
        """
        Precondition:
        n is an integer greater or equal than 2
        Postcondition: function returns an integer: the largest prime factor of n
        """
        self.v.precondition(n>=2 and isinstance(n, int))
        return -1