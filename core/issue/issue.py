from core.models import IssueModel
from core.utility.utility import Utility


class Issue(IssueModel):
    class Meta:
        proxy = True

    def __init__(self, *args, **kwargs):
        super(Issue, self).__init__(*args, **kwargs)

    def response_data(self):
        data = dict()
        data['id'] = self.pk
        data['subject'] = self.subject
        data['description'] = self.description
        data['timestamp'] = self.timestamp
        if self.place:
            data['place'] = self.place

        return data

    @property
    def subject_key(self):
        return self._key(self.subject)

    @property
    def description_key(self):
        return self._key(self.description)

    @property
    def place_key(self):
        return self._key(self.place)

    @staticmethod
    def _key(content):
        return Utility.hash_to_key(content)
