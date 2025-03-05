"""
The prime factors of 13195 are  5, 7 13, and 29.

What is the largest prime factor of the number 600851475143?
"""

import math
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
        sieve = SieveOfEratothenes(n)
        x = sieve.next_prime()
        # check if the floor of log base x of n is the same as log base x of n
        while not self._is_power_of(x, n):
            # do things
            i = 0
            while n%(x**(i+1))==0:
                i+=1

            if i >0:
                n /= x**i

            x = sieve.next_prime()
        
        return x
    
    def _is_power_of(self, b,x):
        m = math.log(x)/math.log(b)
        return math.floor(m) == m
    
    
class SieveOfEratothenes:
    def __init__(self, n):
        self.size = n
        self._sieve = [-1]*(n+1)
        self._sieve[2] = 2
        self._cur = 0

        for i in range(3, n, 2):
            self._sieve[i] = i

        for j in range(3, n, 2):
            if self._sieve[j] != -1:
                for k in range(2*j, n, j):
                    self._sieve[k] = -1;

    def next_prime(self):
        while self._cur <= self.size and self._sieve[self._cur] == -1:
            self._cur += 1
        ans = self._cur
        self._cur +=1
        return ans