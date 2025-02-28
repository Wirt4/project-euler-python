class Validator:

    def precondition(self, evaluation = None, message = "Precondition not met"):
        """
        the evalution is a boolean and it is mandatory
        the message is a string and it is optional

        If the evaluation is False, the function will raise an exception with the message
        if the value of evaluation is True, the function will return None
        """
        if evaluation:
            return None
        raise PreconditionException(message)

class PreconditionException(Exception):
    def __init__(self, message="Precondition not met"):
        self.message = message
        super().__init__(self.message)