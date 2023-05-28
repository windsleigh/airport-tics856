class Plane:
    def __init__(self, id, status, tickets, seats, time, gate):
        self.id = id
        self.status = status
        self.tickets = tickets
        self.seats = seats
        self.time = time
        self.gate = gate
        self.queue = []

    def sell_ticket(self):
        self.tickets -= 1

    def board_plane(self):
        self.seats -= 1

    def has_available_tickets(self):
        return self.tickets > 0

    def print_tickets(self):
        print("tickets lefts:", self.tickets)

    def queue_length(self):
        return len(self.queue)

    def add_passenger(self, passenger):
        self.queue.append(passenger)

    def get_passenger(self):
        return self.queue.pop(0)
