from core.models import UserIssueFiltersModel


class Filter(UserIssueFiltersModel):
    class Meta:
        proxy = True
        ordering = ["user", "pk"]

    def __init__(self, *args, **kwargs):
        super(Filter, self).__init__(*args, **kwargs)