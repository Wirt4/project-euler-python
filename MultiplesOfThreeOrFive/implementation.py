
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
        if not isinstance(factors, list):
            raise Exception("Factors must be a list of integers")
        for factor in factors:
            if not isinstance(factor, int) or factor < 0:
                raise Exception("Factors must be non-negative integers")
        if not isinstance(limit, int) or limit < 0:
            raise Exception("Limit must be a positive integer")
        return 23