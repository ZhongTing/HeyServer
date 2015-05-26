from core.issue.issue import Issue
from core.recommend.recommend_manager import RecommendManager
from django.test import TestCase


class TestRecommendManager(TestCase):
    def setUp(self):
        self._recommend_manager = RecommendManager(None)

    def test_update(self):
        self._recommend_manager.update(Issue.objects.all())