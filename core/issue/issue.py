from core.models import IssueModel
from core.utility.utility import Utility


class Issue(IssueModel):
    class Meta:
        proxy = True

    def __init__(self, *args, **kwargs):
        super(Issue, self).__init__(*args, **kwargs)
        self.__dict__["subject_key"] = Utility.hash_to_key(self.subject)
        self.__dict__["description_key"] = Utility.hash_to_key(self.description)
        self.__dict__["place_key"] = Utility.hash_to_key(self.place)

    def response_data(self):
        data = dict()
        data['id'] = self.pk
        data['subject'] = self.subject
        data['description'] = self.description
        if self.place:
            data['place'] = self.place

        return data