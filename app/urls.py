from app.settings import STATIC_ROOT
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.issue',
    url(r'^api/issue/raise$', 'raise_issue'),
    url(r'^api/issue/fetch$', 'fetch_issue'),
)

urlpatterns += patterns(
    'api.user',
    url(r'^api/user/pull/recommends', 'pull_recommends'),
)

urlpatterns += patterns(
    '',
    url(r'^photo/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT})
)