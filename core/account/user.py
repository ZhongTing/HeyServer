from datetime import datetime

from core.issue.issue import Issue
from core.issue.issue_manager import IssueManager
from core.models import UserModel
from core.recommend.recommend_manager import RecommendManager


class User(UserModel):
    class Meta:
        proxy = True

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._issue_manager = IssueManager(self)
        self._recommend_manager = RecommendManager(self)

        self.update_commends()

    def __str__(self):
        return str(self.__dict__)

    def update_commends(self):
        issues = Issue.objects.all()
        self._recommend_manager.update(issues)

    def raise_issue(self, args):
        self._issue_manager.raise_issue(args)

    def fetch_issue(self, last_issue_id):
        # now = datetime.now()
        # minutes = 1

        issues = list()
        for issue in self._issue_manager.fetch_issue(last_issue_id):
            # issue.timestamp = now
            issues = [issue.response_data()] + issues

            # now -= timedelta(minutes=random.randrange(minutes, minutes * 3))
            # minutes = math.ceil(minutes * 1.5) % (60 * 60)

        return issues

    def get_recommend_list(self):
        return self._recommend_manager.get_commend_list()

