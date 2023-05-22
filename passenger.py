class Passenger:
    def __init__(self, id, plane, checkin, server, time):
        self.__id = id  # ID PASSENGER
        self.__plane = plane  # variable importante es un OBJETO
        self.__checkin = checkin
        self.__server = server
        self.__time = time  # como maneja la llega

    @property
    def get_start(self):
        return self.__start

    @setter.start
    def get_start(self, start):
        self.__start = start

    @property
    def get_finish(self):
        return self.__start

    @setter.finish
    def get_finish(self, finish):
        self.__finish = finish

    def time_spent_in_airport(self):
        return self.finish - self.start
