import threading

from core.account.user import User
from core.models import UserModel
from core.utility.error_exceptions import AuthorizationError, DeviceIdentityExistedError
from core.utility.utility import Utility
from django.db import IntegrityError


class UserManager():
    def __init__(self):
        self.__user_token_cache = {}
        self.update_all_user_recommends()

    def get_user_from_token(self, token, use_cache=True):
        if use_cache and token in self.__user_token_cache:
            return self.__user_token_cache[token]

        try:
            user = User.objects.get(access_token=token)
            self.__user_token_cache[token] = user
            return user

        except UserModel.DoesNotExist:
            raise AuthorizationError()

    def update_all_user_recommends(self):
        for token, user in self.__user_token_cache.iteritems():
            user.update_commends()

        threading.Timer(5, self.update_all_user_recommends).start()

    @staticmethod
    def register(coupon, device_identity):
        user_identity = Utility.hash_to_key(device_identity)
        token = Utility.generate_token()

        try:
            user = User.objects.create(user_id=user_identity, device_identity=device_identity, access_token=token)
        except IntegrityError:
            raise DeviceIdentityExistedError()

        coupon.use()
        return user