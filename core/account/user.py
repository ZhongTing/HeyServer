from core.issue.issue_serializer import IssueSerializer


class User():
    def __init__(self, model):
        self._user = model

    def __str__(self):
        return str(self._user.__dict__)

    def raise_issue(self, args):
        args["user"] = self._user.pk

        serializer = IssueSerializer(data=args)
        print args
        if serializer.is_valid():
            serializer.save()
            return True
        else:
            print serializer.errors
            return False