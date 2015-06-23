from core.filter.filter import Filter
from core.utility.error_exceptions import IssueFilterDuplicate
from django.db import IntegrityError


class FilterManager():
    def __init__(self):
        self._load_all_filters()

    def add_filter(self, user, subject):
        cache = self._get_filter_cache(user)

        try:
            filter_object = Filter.objects.create(user=user, subject=subject)
            cache[filter_object.pk] = filter_object
        except IntegrityError:
            raise IssueFilterDuplicate()
        return filter_object.pk

    def remove_filter(self, user, filter_id):
        cache = self._get_filter_cache(user)
        if filter_id in cache:
            cache.pop(filter_id, None)
            try:
                Filter.objects.get(pk=filter_id).delete()
            except Filter.DoesNotExist:
                pass

    def list_filter(self, user):
        cache = self._get_filter_cache(user)
        filters = list()
        for key, filter_object in cache.iteritems():
            filters.append(filter_object.response_data)
        return filters

    def enable_notification(self, user, filter_id):
        cache = self._get_filter_cache(user)
        print cache
        if filter_id in cache:
            print "in cache"
            filter_object = cache[filter_id]
            filter_object.enabled = True
            filter_object.save()

    def disable_notification(self, user, filter_id):
        cache = self._get_filter_cache(user)
        print cache
        if filter_id in cache:
            print "in cache"
            filter_object = cache[filter_id]
            filter_object.enabled = False
            filter_object.save()

    def _get_filter_cache(self, user):
        user_id = user.pk
        if user_id not in self._user_filter_caches:
            self._user_filter_caches[user_id] = dict()
        return self._user_filter_caches[user_id]

    def _load_all_filters(self):
        self._user_filter_caches = dict()
        filters = Filter.objects.all()
        for filter_object in filters:
            cache = self._get_filter_cache(filter_object.user)
            cache[filter_object.pk] = filter_object

        print self._user_filter_caches