from core.models import UserIssueFiltersModel


class Filter(UserIssueFiltersModel):
    class Meta:
        proxy = True
        ordering = ["user", "pk"]

    def __init__(self, *args, **kwargs):
        super(Filter, self).__init__(*args, **kwargs)

    @property
    def response_data(self):
        data = dict()
        data["id"] = self.pk
        data["subject"] = self.subject
        data["enabled"] = self.enabled

        return data
