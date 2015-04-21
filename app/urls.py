from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.issue',
    url(r'^api/issue/raise$', 'raise_issue'),
    url(r'^api/issue/catch$', 'catch_issue'),
)

urlpatterns += patterns(
    'api.user',
    url(r'^api/user/pull/recommends', 'pull_recommends'),
)
