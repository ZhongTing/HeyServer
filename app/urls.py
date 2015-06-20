from app.settings import STATIC_ROOT
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.issue',
    url(r'^api/issue/raise$', 'raise_issue'),
    url(r'^api/issue/fetch$', 'fetch_issue'),
    url(r'^api/issue/like$', 'issue_like'),
    url(r'^api/issue/regret$', 'issue_regret'),
)

urlpatterns += patterns(
    'api.user',
    url(r'^api/user/pull/recommends$', 'pull_recommends'),
    url(r'^api/user/login$', 'login'),
    url(r'^api/user/register$', 'register'),
    url(r'^api/user/register/android/notification$', 'register_android_notification'),
)

urlpatterns += patterns(
    '',
    url(r'^photo/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT})
)