"""
WSGI config for HeyServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
from core.account.user_manager import UserManager
from core.filter.filter_manager import FilterManager
from core.notification.notification_manager import NotificationManager

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HeyServer.settings")

from django.core.wsgi import get_wsgi_application

user_manager = UserManager()
filter_manager = FilterManager()
notification_manager = NotificationManager(user_manager, filter_manager.filters)

application = get_wsgi_application()
