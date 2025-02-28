class Validator:

    def precondition(self, evaluation = False, message = "Precondition not met"):
        """
        the evalution is a boolean and it is mandatory
        the message is a string and it is optional

        If the evaluation is False, the function will raise an exception with the message
        if the value of evaluation is True, the function will return None
        """
        self._evaluate_and_raise(PreconditionException, evaluation, message)
    
    def postcondition(self, evaluation = False, message = None):
        """
        the evalution is a boolean and it is mandatory
        the message is a string and it is optional

        If the evaluation is False, the function will raise an exception with the message
        if the value of evaluation is True, the function will return None
        """
        self._evaluate_and_raise(PostconditionException, evaluation, message)
    
    def _evaluate_and_raise(self,  exception, evaluation=False, message=None):
        if evaluation:
            return None
        if message:
            raise exception(message)
        raise exception()

class PreconditionException(Exception):
    def __init__(self, message="Precondition not met"):
        self.message = message
        super().__init__(self.message)

class PostconditionException(Exception):
    def __init__(self, message="Postcondition not met"):
        self.message = message
        super().__init__(self.message)

