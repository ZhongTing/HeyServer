from core.issue.issue_manager import IssueManager
from core.models import UserLikeIssuesModel


class UserLikeIssues():
    def __init__(self, user):
        self._user = user

    def add_issue(self, issue_id):
        relation = self._get_user_like_issue_relation(issue_id)
        if relation is None:
            issue = IssueManager.get_issue_from_id(issue_id)
            UserLikeIssuesModel.objects.create(user=self._user, issue=issue)

    def remove_issue(self, issue_id):
        relation = self._get_user_like_issue_relation(issue_id)
        if relation is not None:
            relation.delete()

    def _get_user_like_issue_relation(self, issue_id):
        try:
            return UserLikeIssuesModel.objects.get(user=self._user, issue=issue_id)

        except UserLikeIssuesModel.DoesNotExist:
            return None