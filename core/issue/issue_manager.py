from core.issue.issue import Issue
from core.issue.issue_serializer import IssueSerializer
from core.issue.like_issue import LikeIssue
from core.utility.error_exceptions import SerializerError, IssueNotFound


class IssueManager():
    def __init__(self, user):
        self._user = user

    @staticmethod
    def fetch_issue(last_issue_id):
        return Issue.objects.filter(pk__gt=last_issue_id).all()

    @staticmethod
    def fetch_popular_issue():
        return Issue.objects.filter(good__gte=1).order_by('-good', '-pk')

    @staticmethod
    def fetch_like_issue():
        return LikeIssue.objects.filter(good__gte=1).all()

    def raise_issue(self, args):
        args["user"] = self._user.pk

        serializer = IssueSerializer(data=args)
        if serializer.is_valid():
            issue = serializer.save()
            issue.save_photo(args["photo"])
        else:
            raise SerializerError(serializer.errors)

    @staticmethod
    def get_issue_from_id(issue_id):
        try:
            return Issue.objects.get(pk=issue_id)
        except Issue.DoesNotExist:
            raise IssueNotFound()