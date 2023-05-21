class Plane:
    seats = 100

    def __init__(self, id, status, lane, seats):
        self.id = id
        self.status = status
        self.lane = lane
        self.seats = seats

    def add_passenger(self):
        self.seats -= 1

    def has_available_seats(self):
        return self.seats > 0
