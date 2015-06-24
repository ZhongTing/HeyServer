# coding:utf8
from core.account.user import User
from core.notification.android_notification_object import AndroidNotificationObject
from core.notification.notification_manager import NotificationQueue
from django.test import TestCase


class TestAnything(TestCase):
    def setUp(self):
        pass

    def test_notification(self):
        user_id = 12345
        device_identity = "test"
        notification_token = "fk4rBlufsek:APA91bHPot3ZJAA0zAto1n_2aR-wcZf2LGAi6VFX4STVLYWY5RB5QNzL8bI4E2pkkBf0NZ7hgHCPoicr40XwdDphBl3jGiPzl5iv6SpOMZ5Q7IytK9PFgI_XtaeHz-KlTGTyEovY5jZN"
        # notification_token = "dJjkYSurmMU:APA91bFO1skpGpYnwqq0LwJr4LvryzKynNGWgVlmZVRI6yqSrS4uAKFbcAVmvHUGwdFiwEMFQ1YzYlso4MTcIKsO68YoKd7UHXKO8RECN_MZyHynRfb6c2PCXekWTvK__4paFWAkpNcE"
        user = User.objects.create(user_id=user_id, device_identity=device_identity,
                                   notification_token=notification_token)
        notification = NotificationQueue(5)
        for i in range(1, 10):
            notification.push(AndroidNotificationObject(user, "起床尿尿囉 %d" % i))

    def test_gcm_python(self):
        pass