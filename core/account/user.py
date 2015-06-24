from core.account.user_like_issues import UserLikeIssues
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
        self._like_issues = UserLikeIssues(self)

        self.update_commends()

    def __str__(self):
        return str(self.__dict__)

    @property
    def token(self):
        return {
            "token": self.access_token
        }

    def update_commends(self):
        issues = Issue.objects.all()
        self._recommend_manager.update(issues)

    def raise_issue(self, args):
        return self._issue_manager.raise_issue(args)

    def fetch_issue(self, last_issue_id):
        issues = list()
        for issue in self._issue_manager.fetch_issue(last_issue_id):
            issues = [issue.response_data()] + issues

        return issues

    def fetch_popular_issue(self):
        issues = list()
        for issue in self._issue_manager.fetch_popular_issue():
            issues = [issue.response_data()] + issues

        return issues

    def fetch_like_issue(self):
        issues = list()
        for issue in self._issue_manager.fetch_like_issue():
            issues = [issue.response_data()] + issues

        return issues

    def get_recommend_list(self):
        return self._recommend_manager.get_commend_list()

    def like_issue(self, issue_id):
        return self._like_issues.add_issue(issue_id)

    def regret_issue(self, issue_id):
        return self._like_issues.remove_issue(issue_id)

    def update_notification_token(self, notification_token):
        self.notification_token = notification_token
        self.save()