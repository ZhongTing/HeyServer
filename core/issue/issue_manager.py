from core.issue.issue import Issue
from core.issue.issue_serializer import IssueSerializer
from core.utility.error_exceptions import SerializerError


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
            serializer.save()
        else:
            raise SerializerError(serializer.errors)