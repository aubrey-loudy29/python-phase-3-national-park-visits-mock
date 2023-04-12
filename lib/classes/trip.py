class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        Trip.all.append(self)
        if type(start_date) == str :
            self.start_date = start_date
        if type(end_date) == str :
            self.end_date = end_date

    @classmethod
    def get_all(cls) :
        return cls.all
