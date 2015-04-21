from core.issue.issue_serializer import IssueSerializer
from core.utility.error_exceptions import Error


class User():
    def __init__(self, model):
        self._user = model

    def __str__(self):
        return str(self._user.__dict__)

    def raise_issue(self, args):
        args["user"] = self._user.pk

        serializer = IssueSerializer(data=args)
        if serializer.is_valid():
            serializer.save()
        else:
            raise Error(serializer.errors)

    def pull_recommends(self):
        return {}