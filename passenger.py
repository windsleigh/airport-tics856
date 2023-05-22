class Passenger:
    start = 0
    finish = 0
    plane = getPlane(event.planeId)

    def __init__(self, id, plane, checkin, server, time):
        self.id = id  # ID PASSENGER
        self.plane = plane  # variable importante es un OBJETO
        self.checkin = checkin
        self.server = server
        self.time = time

    def time_spent_in_airport(self):
        return self.finish - self.start
