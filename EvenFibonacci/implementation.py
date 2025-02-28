class Fibonacci:
    
    def get_even_sum(self, limit):
        """
        precondition:
        limit is a natural number.  

        postcondition:
        get_even_sum returns a natural number, the sum of all even Fibonacci numbers less than or equal to the limit  
        """

       
        if not self._is_valid_integer(limit):
            raise PreconditionException("Limit must be a natural number")
        return -1
    
    def _is_valid_integer(self, limit):
        if limit <=0:
            return False
        return isinstance(limit, int)
    
class PreconditionException(Exception):
    """Base custom exception class"""
    def __init__(self, message="Precondition not met"):
        self.message = message
        super().__init__(self.message)