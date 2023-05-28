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
            # print("overbooked plane: ", random_plane.id)
            return random_plane
        else:
            print("this sucks")

    # Choose a random plane from the list of planes that have available tickets
    random_plane = random.choice(planes_with_seats)
    # print("plane: ", random_plane.id)
    # Sell a ticket for the chosen plane
    random_plane.sell_ticket()
    # random_plane.print_tickets()

    return random_plane
