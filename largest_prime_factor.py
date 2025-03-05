"""
The prime factors of 13195 are  5, 7 13, and 29.

What is the largest prime factor of the number 600851475143?
"""

import math
import queue
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
        sieve = PrimeNumberGenerator()
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
    
    
class PrimeNumberGenerator:
    def __init__(self):
        self.all_primes = {2,3}
        self.q = queue.Queue()
        self.q.put(2)
        self.q.put(3)
        self.largest_prime = 3

    def next_prime(self):
        self.largest_prime += 2
        while (self._is_divisible(self.largest_prime)):
            self.largest_prime += 2

        self.all_primes.add(self.largest_prime)
        self.q.put(self.largest_prime)
        return self.q.get()
    
    def _is_divisible(self, n):
        for prime in self.all_primes:
            if n%prime == 0:
                return True
        return False
       