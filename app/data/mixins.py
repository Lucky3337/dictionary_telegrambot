class ActionsMixin:
    @property
    def actions(self):
        return [item[0] for item in self.data]
