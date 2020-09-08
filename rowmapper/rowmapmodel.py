class RowMapModel:
    def __init__(self, *args):
        for value in args:
            self.name = value[0]
            self.city = value[2]
            self.salary = value[3]
