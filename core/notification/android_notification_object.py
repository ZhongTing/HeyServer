from app.settings import ANDROID_NOTIFICATION_API_KEY
from core.account.user import User
from gcm import GCM
from gcm.gcm import GCMNotRegisteredException, GCMUnavailableException


class AndroidNotificationObject():
    def __init__(self, user, message):
        self._user = user
        self._data = {'message': message}
        self._gcm = GCM(ANDROID_NOTIFICATION_API_KEY)

    def __str__(self):
        return "\n[Object] %d -> %s" % (self._user.pk, self._data['message'])

    def send(self):
        token = self._user.notification_token
        if token:
            try:
                canonical_id = self._gcm.json_request(registration_ids=[token], data=self._data)
                if canonical_id:
                    User.objects.filter(pk=self._user.pk).update(notification_token=canonical_id)

            except GCMNotRegisteredException:
                User.objects.filter(pk=self._user.pk).update(notification_token="")

            except GCMUnavailableException:
                pass