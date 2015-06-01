from core.issue.issue import Issue


class RecommendManager():
    def __init__(self, user):
        self._user = user
        self.subjects = dict()
        self.descriptions = dict()
        self.places = dict()

        self.update(Issue.objects.all())

    def update(self, issues):
        for issue in issues:
            self._add_subject(issue)
            self._add_description(issue)
            self._add_place(issue)

    @staticmethod
    def _add(collection, key, value):
        if key in collection:
            collection[key]["count"] += 1
        else:
            collection[key] = {
                "content": value,
                "count": 1
            }

    def _add_subject(self, issue):
        self._add(self.subjects, issue.subject_key, issue.subject)
        self.descriptions[issue.subject_key] = {}
        self.places[issue.subject_key] = {}

    def _add_description(self, issue):
        self._add(self.descriptions[issue.subject_key], issue.description_key, issue.description)

    def _add_place(self, issue):
        self._add(self.places[issue.subject_key], issue.place_key, issue.place)

    def get_commend_list(self):
        recommends = dict()
        recommends["subjects"] = dict()
        for key, subject in self.subjects.iteritems():
            subject_content = subject["content"]
            recommends["subjects"][subject_content] = {
                "descriptions": list(),
                "places": list(),
            }
            for none, description in self.descriptions[key].iteritems():
                if description["content"] is not None:
                    recommends["subjects"][subject_content]["descriptions"].append(description["content"])
            for none, place in self.places[key].iteritems():
                if place["content"] is not None:
                    recommends["subjects"][subject_content]["places"].append(place["content"])
        return recommends