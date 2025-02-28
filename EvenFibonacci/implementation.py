from Validator.implementation import Validator


class Fibonacci:
    def __init__(self):
        self.validator = Validator()
    
    def get_even_sum(self, limit):
        """
        precondition:
        limit is a natural number.  

        postcondition:
        get_even_sum returns a natural number, the sum of all even Fibonacci numbers less than or equal to the limit  
        """

        self.validator.precondition(self._is_valid_integer(limit), "Limit must be a natural number")
        return -1
    
    def _is_valid_integer(self, limit):
        if limit <=0:
            return False
        return isinstance(limit, int)
    
