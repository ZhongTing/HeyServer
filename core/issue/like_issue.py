from core.models import IssueModel


class LikeIssue(IssueModel):
    class Meta:
        proxy = True
        ordering = ["-good", "-pk"]

    def __init__(self, *args, **kwargs):
        super(LikeIssue, self).__init__(*args, **kwargs)

    def response_data(self):
        data = dict()
        data['id'] = self.pk
        data['like'] = self.good

        return data
