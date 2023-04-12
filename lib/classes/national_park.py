from .trip import Trip

class NationalPark:

    def __init__(self, name) :
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, input):
        if type(input) == str and not hasattr(self, 'name') :
            self._name = input

    name = property(get_name, set_name)

    def trips(self):
        return [trip for trip in Trip.get_all() if trip.national_park == self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(self.visitors(), key = visitors.count)