class User():
    def __init__(self, model):
        self._model = model

    def __str__(self):
        return str(self._model.__dict__)

    def raise_issue(self, issue):
        pass