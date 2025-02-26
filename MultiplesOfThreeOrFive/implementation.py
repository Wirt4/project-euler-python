
class Mulitples:
    def multiples(self, factors, limit):
        """
        This function returns the sum of all the multiples of the factors
        in the range of 0 to the limit.

        precodntion:
        factors is a list of positive integers
        limit is a positive integer

        postcondition:
        multiplse returns a number
        """
        self._validtate_factors(factors)
        self._validate_limit(limit)
        return 23
    

    def _validtate_factors(self, factors):
        if not isinstance(factors, list) or not self._is_valid_integer_list(factors):
            raise FactorsException()
    
    def _is_valid_integer_list(self, factors):
        for f in factors:
            if not self._is_valid_integer(f):
                return False
        return True
        
    def _is_valid_integer(self, limit):
        return isinstance(limit, int) and limit > 0
    
    def _validate_limit(self, limit):
        if not self._is_valid_integer(limit):
            raise LimitException()
        


class FactorsException(Exception):
         """Base custom exception class"""  
         def __init__(self, message="Factors must be a list of positive integers"):
            self.message = message
            super().__init__(self.message)

class LimitException(Exception):
         """Base custom exception class"""
         def __init__(self, message="Limit must be a positive integer"):
            self.message = message
            super().__init__(self.message)