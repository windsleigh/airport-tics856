class Plane:
    __total_planes = []

    def __init__(self, id, status, lane, seats):
        self.id = id  # ID PLANE
        self.status = status
        self.lane = lane
        self.seats = seats
        Plane.__total_planes.append(self)

    @property
    def get_total_planes():
        return Plane.__total_planes

    def add_passenger(self):
        self.seats -= 1

    def has_available_seats(self):
        return self.seats > 0
