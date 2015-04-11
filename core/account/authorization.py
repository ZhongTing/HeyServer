from core.account.user_manager import UserManager


class Authorization():
    def __init__(self, request):
        self._error_message = None
        self._user = None

        self._auth_request(request)

    @property
    def is_valid(self):
        return self._error_message is None

    @property
    def error_message(self):
        return self._error_message

    @property
    def get_user(self):
        return self._user

    def _auth_request(self, request):
        if "http_authorization".upper() in request.META:
            token = request.META["http_authorization".upper()]
            print "Request Token: ", token
            
            self._user = UserManager.get_user_from_token(token)
            print "User: ", self._user

        else:
            self._error_message = "authorization missing!"