import random


class Passenger:
    def __init__(self, id, plane, checkin, server, time, arrival_time, gender):
        self.id = id
        self.plane = plane
        self.checkin = checkin
        self.server = server
        self.time = time
        self.arrival_time = arrival_time
        self.gender = gender
