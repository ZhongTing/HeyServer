from datetime import datetime

from app.settings import STATIC_ROOT, STATIC_URL, SERVER_URL
from core.models import IssueModel
from core.utility.utility import Utility
import os


class Issue(IssueModel):
    class Meta:
        proxy = True
        ordering = ["-pk"]

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
        if self.photo_url:
            data["photoURL"] = "%s%s" % (SERVER_URL, self.photo_url)

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

    def save_photo(self, photo_file):
        if photo_file is not None:
            photo_url, photo_path = self._create_photo_info()

            save_file = open(photo_path, "wb")
            for chunk in photo_file:
                save_file.write(chunk)
            save_file.close()

            self.photo_url = photo_url
            self.save()

    def _create_photo_info(self):
        path = "issue/%s/%s.png"
        today = self.timestamp.strftime("%Y%m%d")
        filename = Utility.hash_to_key(datetime.utcnow())

        path = path % (today, filename)
        photo_url = STATIC_URL + path
        photo_path = os.path.join(STATIC_ROOT, path)
        folder = os.path.dirname(photo_path)

        if not os.path.exists(folder):
            os.makedirs(folder)

        return photo_url, photo_path
