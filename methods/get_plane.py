import random
from global_variables import *
from objects.plane import Plane


def get_plane():
    global board_gates
    global plane_queue
    # puertas : son los aviones que estan siendo abordados
    # cola_aviones : son los aviones que se agendaron pero no habia espacio en las puertas

    planes_without_seats = []

    for idx, plane in enumerate(board_gates):
        if not plane.has_available_seats():
            planes_without_seats.append(board_gates[idx].id)
    for idx, plane in enumerate(board_gates):
        if not plane.has_available_seats():
            planes_without_seats.append(plane_queue[idx].id)

    # lanzamos un dado
    assigned_plane = random.choice(
        [
            i
            for i in range(board_gates[0], board_gates[-1] + len(plane_queue))
            if i not in planes_without_seats
        ]
    )

    for idx, plane in enumerate(board_gates):
        if plane and plane.id == assigned_plane:
            board_gates[idx].add_passenger()
            print("added to gates")
            print(board_gates[idx].seats)
            return board_gates[idx]

    for idx, plane in enumerate(plane_queue):
        if plane and plane.id == assigned_plane:
            plane_queue[idx].add_passenger()
            print("added to plane")
            print(plane_queue[idx].seats)
            return plane_queue[idx]

    # si no existe el avion y hay espacio en la cola se agrega un avion al
    queue_count = sum(1 for plane in plane_queue if plane is not None)
    new_plane = Plane(plane_queue[queue_count].id + 1, "arriving", seats)

    # Hay que agregarlo a la puerta de aviones si hay una libre o a la cola de aviones si hay una libre
    # for idx, plane in enumerate(board_gates):
    #     if plane is not None:
    #         new_plane.add_passenger()
    #         board_gates[idx] = new_plane
    #         return new_plane
    for idx, plane in enumerate(plane_queue):
        if plane is not None:
            new_plane.add_passenger()
            plane_queue[idx] = new_plane
            return new_plane
