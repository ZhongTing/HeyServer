class RecommendManager():
    def __init__(self, user):
        self._user = user
        self._recommends = dict()

    def update(self, issues):
        for issue in issues:
            if issue.subject_key in self._recommends:
                self._recommends[issue.subject_key]["count"] += 1

            else:
                self._recommends[issue.subject_key] = {
                    "content": issue.subject,
                    "descriptions": dict(),
                    "places": dict(),
                    "count": 1
                }

            subject = self._recommends[issue.subject_key]
            if issue.description_key in subject["descriptions"]:
                description = subject["descriptions"][issue.description_key]
                description["count"] += 1
            else:
                subject["descriptions"][issue.description_key] = {
                    "content": issue.description,
                    "count": 1
                }

            if issue.place_key is not None:
                if issue.place_key in subject["places"]:
                    place = subject["places"][issue.place_key]
                    place["count"] += 1
                else:
                    subject["places"][issue.place_key] = {
                        "content": issue.place,
                        "count": 1
                    }

    def get_commend_list(self):
        return self._recommends