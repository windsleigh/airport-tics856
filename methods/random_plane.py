import random
from config import gates


def random_plane():
    global gates

    # Create a list of planes that have tickets available
    planes_with_seats = [
        plane for plane in gates if plane and plane.has_available_tickets()
    ]

    # overbooking
    if len(planes_with_seats) == 0:
        random_plane = random.choice(gates)
        if random_plane is not None:
            random_plane.sell_ticket()
            return random_plane
        else:
            print("this sucks")

    # Choose a random plane from the list of planes that have available tickets
    random_plane = random.choice(planes_with_seats)

    # Sell a ticket for the chosen plane
    random_plane.sell_ticket()

    return random_plane
