class Passenger:
    start = 0
    finish = 0

    def __init__(self, id, plane, checkin, server, time):
        self.id = id
        self.plane = plane
        self.checkin = checkin
        self.server = server
        self.time = time

    def time_spent_in_airport(self):
        return self.finish - self.start
