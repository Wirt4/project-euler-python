
class Multiples:
    def multiples(self, factors, limit):
        """
        This function returns the sum of all the multiples of the factors
        in the range of 1 to the limit. Natural numbers are the only valid

        precodntion:
        factors is a list of natural numbers
        limit is a natural number

        We will not count 0 as a natural number

        postcondition:
        multiple returns a natural number
        """
        self._validate_factors(factors)
        self._validate_limit(limit)

        n = set()

        for f in factors:
            i=0
            while i < limit:
                n.add(i)
                i += f

        s = sum(n)
        self._validate_return(s)
        return s
    

    def _validate_factors(self, factors):
        if not isinstance(factors, list) or not self._is_valid_integer_list(factors):
            raise FactorsException()
    
    def _is_valid_integer_list(self, factors):
        for f in factors:
            if not self._is_valid_integer(f):
                return False
        return True
        
    def _is_valid_integer(self, limit):
        if limit <=0:
            return False
        return isinstance(limit, int)
    
    def _validate_limit(self, limit):
        if not self._is_valid_integer(limit):
            raise LimitException()
        
    def _validate_return(self, result):
        if not self._is_valid_integer(result):
            raise ReturnException()

class FactorsException(Exception):
         """Base custom exception class"""  
         def __init__(self, message="Factors must be a natural number"):
            self.message = message
            super().__init__(self.message)

class LimitException(Exception):
         """Base custom exception class"""
         def __init__(self, message="Limit must be a natural number"):
            self.message = message
            super().__init__(self.message)

class ReturnException(Exception):
         """Base custom exception class"""  
         def __init__(self, message="Return value must be a natural number"):
            self.message = message
            super().__init__(self.message)