from core.account.user import User
from core.models import UserModel
from core.utility.error_exceptions import AuthorizationError


class UserManager():
    def __init__(self):
        self.__user_token_cache = {}

    def get_user_from_token(self, token, use_cache=True):
        if use_cache and token in self.__user_token_cache:
            return self.__user_token_cache[token]

        try:
            user = User.objects.get(access_token=token)
            self.__user_token_cache[token] = user
            return user

        except UserModel.DoesNotExist:
            raise AuthorizationError()


user_manager = UserManager()