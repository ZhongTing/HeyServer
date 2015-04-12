class ErrorMessageTemplate():
    def __init__(self):
        pass

    @property
    def parameter_missing(self):
        return "parameter missing!"

    @property
    def authorization_error(self):
        return "authorization error!"


ErrorMessage = ErrorMessageTemplate()