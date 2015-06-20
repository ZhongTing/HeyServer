from core.issue.issue import Issue
from core.issue.issue_serializer import IssueSerializer
from core.utility.error_exceptions import SerializerError, IssueNotFound


class IssueManager():
    def __init__(self, user):
        self._user = user

    @staticmethod
    def fetch_issue(last_issue_id):
        return Issue.objects.filter(pk__gt=last_issue_id).all()

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