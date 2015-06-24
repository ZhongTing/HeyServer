import threading

from core.account.user import User
from core.models import UserModel
from core.utility.error_exceptions import AuthorizationError, DeviceIdentityExistedError
from core.utility.utility import Utility
from django.db import IntegrityError


class UserManager():
    def __init__(self):
        self._user_cache_by_token = {}
        self._user_cache_by_identity = {}
        self.update_all_user_recommends()

    def get_user_from_token(self, token, use_cache=True):
        if use_cache and token in self._user_cache_by_token:
            return self._user_cache_by_token[token]

        try:
            user = User.objects.get(access_token=token)
            self._user_cache_by_token[user.access_token] = user
            self._user_cache_by_identity[user.pk] = user
            return user

        except UserModel.DoesNotExist:
            raise AuthorizationError()

    def get_users_notification_token(self, user_ids):
        tokens = list()
        for user_id in user_ids:
            user = self.get_user_from_identity(user_id)
            if user and user.token:
                tokens.append(user.token)
        return tokens

    def get_user_from_identity(self, user_identity):
        if user_identity in self._user_cache_by_identity:
            return self._user_cache_by_identity[user_identity]

        try:
            user = User.objects.get(user_id=user_identity)
            self._user_cache_by_token[user.access_token] = user
            self._user_cache_by_identity[user.pk] = user
            return user

        except UserModel.DoesNotExist:
            return None

    def get_user_from_device_identity(self, device_identity):
        user_identity = Utility.hash_to_key(device_identity)
        user = self.get_user_from_identity(user_identity)
        if not user:
            raise DeviceIdentityExistedError()
        return user

    def update_all_user_recommends(self):
        for token, user in self._user_cache_by_token.iteritems():
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