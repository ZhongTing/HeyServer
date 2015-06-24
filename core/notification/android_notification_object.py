from app.settings import ANDROID_NOTIFICATION_API_KEY
from gcm import GCM
from gcm.gcm import GCMNotRegisteredException, GCMUnavailableException


class AndroidNotificationObject():
    def __init__(self, user_manager, filters, user_id, issue_id, message):
        self._filters = filters
        self._user_id = user_id
        self._issue_id = issue_id
        self._user_manager = user_manager
        self._data = {'message': message, 'issueId': issue_id}
        self._gcm = GCM(ANDROID_NOTIFICATION_API_KEY)

    def __str__(self):
        return "\n[Object] -> %s" % (self._data['message'])

    def send(self):
        user_ids = self._find_follow_users(self._data['message'])
        tokens = self._user_manager.get_users_notification_token(user_ids)

        if len(tokens) > 0:
            print tokens
            try:
                self._gcm.json_request(registration_ids=tokens, data=self._data)

            except GCMNotRegisteredException:
                pass

            except GCMUnavailableException:
                pass

    def _find_follow_users(self, message):
        follow_users = list()
        for user_id, user_filter in self._filters.iteritems():
            if user_id == self._user_id:
                continue
            for filter_id, filter_object in user_filter.iteritems():
                if filter_object.enabled and filter_object.subject.upper() in message.upper():
                    follow_users.append(user_id)
        return follow_users
