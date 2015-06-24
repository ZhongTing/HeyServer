from app.settings import ANDROID_NOTIFICATION_API_KEY
from gcm import GCM
from gcm.gcm import GCMNotRegisteredException, GCMUnavailableException


class AndroidNotificationObject():
    def __init__(self, user_manager, filters, message):
        self._filters = filters
        self._user_manager = user_manager
        self._data = {'message': message}
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

    def _find_follow_users(self, subject):
        print "find_follow_user", subject
        follow_users = list()
        for user_id, user_filter in self._filters.iteritems():
            for filter_id, filter_object in user_filter.iteritems():
                print user_id, filter_id, filter_object
                if filter_object.enabled and filter_object.subject in subject:
                    follow_users.append(user_id)
        print "finish finding follow users", follow_users, "\n"
        return follow_users
