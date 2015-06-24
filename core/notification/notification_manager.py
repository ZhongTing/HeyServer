from app.settings import NOTIFICATION_THREAD_MAX_COUNT
from core.notification.android_notification_object import AndroidNotificationObject
from core.utility.notification_queue import NotificationQueue


class NotificationManager(NotificationQueue):
    def __init__(self, user_manager, filters):
        NotificationQueue.__init__(self, NOTIFICATION_THREAD_MAX_COUNT)
        self._user_manager = user_manager
        self._filters = filters

    def push(self, user, issue):
        user_id = user.pk
        issue_id = issue.pk
        message = issue.subject + issue.description
        self._push(AndroidNotificationObject(self._user_manager, self._filters, user_id, issue_id, message))