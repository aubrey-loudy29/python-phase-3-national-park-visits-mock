from .trip import Trip

class Visitor:

    def __init__(self, name) :
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, input):
        if type(input) == str and not hasattr(self, 'name') and 1 <= len(input) <= 15 :
            self._name = input

    name = property(get_name, set_name)

    def trips(self):
        return [trip for trip in Trip.get_all() if trip.visitor == self]

    def nationalparks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    def create_trip(visitor, national_park, start_date, end_date):
        Trip(visitor, national_park, start_date, end_date)