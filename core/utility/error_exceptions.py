class Error(Exception):
    def __init__(self, message="unknown error!"):
        self._message = message

    @property
    def message(self):
        return self._message


class AuthorizationError(Error):
    def __init__(self):
        super(AuthorizationError, self).__init__("authorization fail!")


class ParameterError(Error):
    def __init__(self):
        super(ParameterError, self).__init__("parameter missing!")