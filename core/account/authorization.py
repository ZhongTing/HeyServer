from core.account.user import User


class Authorization():
    def __init__(self, request):
        self._error_message = None
        self._user = None

        self.auth_request(request)

    def is_valid(self):
        return self._error_message is None

    @property
    def error_message(self):
        return self._error_message

    def auth_request(self, request):
        if "http_authorization".upper() in request.META:
            self._user = User()

        else:
            self._error_message = "authorization missing!"

    def get_user(self):
        return self._user