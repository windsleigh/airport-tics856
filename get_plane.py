import random
from main import gates, seats
from plane import Plane


def get_plane(passenger, plane_queue, FEL):
    global gates

    planes_without_seats = []

    for idx, plane in enumerate(gates):
        if not plane.has_available_seats():
            planes_without_seats.append(gates[idx].id)
    for idx, plane in enumerate(gates):
        if not plane.has_available_seats():
            planes_without_seats.append(plane_queue[idx].id)

    assigned_plane = random.choice(
        [
            i
            for i in range(gates[0], gates[-1] + len(plane_queue))
            if i not in planes_without_seats
        ]
    )

    for idx, plane in enumerate(gates):
        if plane and plane.id == assigned_plane:
            gates[idx].add_passenger()
            passenger.plane = gates[idx]

    for idx, plane in enumerate(plane_queue):
        if plane and plane.id == assigned_plane:
            plane_queue[idx].add_passenger()
            passenger.plane = plane_queue[idx]

    # si no existe el avion y hay espacio en la cola se agrega un avion al
    queue_count = sum(1 for plane in plane_queue if plane is not None)
    queue_count = 3

    new_plane = Plane(plane_queue[queue_count].id + 1, "arriving", seats)

    # tengo que agregar al avion a la fel sin que afecte el clock
    fel = [passenger(1), avion(1), avion(1.5), passeger(1.2)]  # ejemplo
    # FEL de aviones?
    # dos clocks?
    passenger.plane = new_plane
    return passenger
