"""
WSGI config for HeyServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
from app.settings import NOTIFICATION_THREAD_MAX_COUNT
from core.account.user_manager import UserManager
from core.notification.notification_manager import NotificationManager

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HeyServer.settings")

from django.core.wsgi import get_wsgi_application

user_manager = UserManager()
notification_manager = NotificationManager(NOTIFICATION_THREAD_MAX_COUNT)

application = get_wsgi_application()
