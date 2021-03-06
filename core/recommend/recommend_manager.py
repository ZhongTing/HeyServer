class RecommendManager():
    def __init__(self, user):
        self._user = user
        self.subjects = dict()
        self.descriptions = dict()
        self.places = dict()

    def update(self, issues):
        self.subjects.clear()
        self.descriptions.clear()
        self.places.clear()

        for issue in issues:
            if not issue.privacy_mode:
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
        recommends = dict()

        recommend_subjects = recommends["subjects"] = list()
        subjects = list(sorted(self.subjects.items(), key=lambda s: -s[1]["count"]))
        for key, subject in subjects:
            subject_object = {
                "content": subject["content"],
                "count": subject["count"],
                "descriptions": list(),
                "places": list(),
            }
            recommend_subjects.append(subject_object)

            descriptions = list(sorted(subject["descriptions"].items(), key=lambda s: -s[1]["count"]))
            for description in descriptions:
                subject_object["descriptions"].append(description[1]["content"])

            places = list(sorted(subject["places"].items(), key=lambda s: -s[1]["count"]))
            for place in places:
                if place[1]["content"] is None:
                    continue
                subject_object["places"].append(place[1]["content"])

        recommend_descriptions = recommends["descriptions"] = list()
        descriptions = list(sorted(self.descriptions.items(), key=lambda s: -s[1]["count"]))
        for key, description in descriptions:
            recommend_descriptions.append(description["content"])

        recommend_places = recommends["places"] = list()
        places = list(sorted(self.places.items(), key=lambda s: -s[1]["count"]))
        for key, place in places:
            if place["content"] is None:
                continue
            recommend_places.append(place["content"])

        return recommends