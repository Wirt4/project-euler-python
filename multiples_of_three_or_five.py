
from validator import Validator


class Multiples:
    def __init__(self):
        self.validator = Validator()
        
    def multiples(self, factors, limit):
        """
        Multiples of 3 or 5 
        Problem 1
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and9 . The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.

        This function returns the sum of all the multiples of the factors
        in the range of 1 to the limit. Natural numbers are the only valid

        precodntion:
        factors is a list of natural numbers
        limit is a natural number

        We will not count 0 as a natural number

        postcondition:
        multiple returns a natural number
        """
        self.validator.precondition(isinstance(factors, list) and self._is_valid_integer_list(factors), "Factors must be a list of natural numbers")
        self.validator.precondition(self._is_valid_integer(limit), "Limit must be a natural number")

        n = set()

        for f in factors:
            i=0
            while i < limit:
                n.add(i)
                i += f

        s = sum(n)
        self.validator.postcondition(self._is_valid_integer(s), "Sum must be a natural number")
        return s
    
    def _is_valid_integer_list(self, factors):
        for f in factors:
            if not self._is_valid_integer(f):
                return False
        return True
        
    def _is_valid_integer(self, limit):
        if limit <=0:
            return False
        return isinstance(limit, int)
