from app.settings import ANDROID_NOTIFICATION_API_KEY
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
                self._gcm.json_request(registration_ids=[token], data=self._data)

            except GCMNotRegisteredException:
                pass

            except GCMUnavailableException:
                pass