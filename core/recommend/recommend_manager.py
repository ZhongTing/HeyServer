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

    def _add_description(self, issue):
        self._add(self.descriptions, issue.description_key, issue.description)

        subject = self.subjects[issue.subject_key]
        if "descriptions" not in subject:
            subject["descriptions"] = dict()
        subject["descriptions"][issue.description_key] = self.descriptions[issue.description_key]

    def _add_place(self, issue):
        self._add(self.places, issue.place_key, issue.place)

        subject = self.subjects[issue.subject_key]
        if "places" not in subject:
            subject["places"] = dict()
        subject["places"][issue.place_key] = self.places[issue.place_key]

    def get_commend_list(self):
        subjects = list(reversed(sorted(self.subjects.items(), key=lambda s: s[1]["count"])))

        recommends = dict()
        recommend_subjects = recommends["subjects"] = dict()
        for key, subject in subjects:
            subject_content = subject["content"]
            recommend_subjects[subject_content] = {
                "descriptions": list(),
                "places": list(),
            }

            descriptions = list(reversed(sorted(subject["descriptions"].items(), key=lambda s: s[1]["count"])))
            for description in descriptions:
                recommend_subjects[subject_content]["descriptions"].append(description[1]["content"])

            places = list(reversed(sorted(subject["places"].items(), key=lambda s: s[1]["count"])))
            for place in places:
                recommend_subjects[subject_content]["places"].append(place[1]["content"])

        return recommends