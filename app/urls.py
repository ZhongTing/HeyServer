from app.settings import STATIC_ROOT
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.issue',
    url(r'^api/issue/raise$', 'raise_issue'),
    url(r'^api/issue/fetch$', 'fetch_issue'),
    url(r'^api/issue/like$', 'issue_like'),
    url(r'^api/issue/regret$', 'issue_regret'),
    url(r'^api/issue/like/fetch', 'fetch_like_issue'),
)

urlpatterns += patterns(
    'api.user',
    url(r'^api/user/pull/recommends$', 'pull_recommends'),
    url(r'^api/user/login$', 'login'),
    url(r'^api/user/register$', 'register'),
    url(r'^api/user/register/android/notification$', 'register_android_notification'),
)

urlpatterns += patterns(
    'api.filter',
    url(r'^api/filter/list', 'list_filter'),
    url(r'^api/filter/add', 'add_filter'),
    url(r'^api/filter/remove', 'remove_filter'),
    url(r'^api/filter/notification/enable', 'enable_filter_notification'),
    url(r'^api/filter/notification/disable', 'disable_filter_notification'),
)

urlpatterns += patterns(
    '',
    url(r'^photo/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT})
)