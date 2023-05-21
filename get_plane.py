from main import gates, plane_queue


def get_plane(passenger):
    global gates
    global plane_queue

    queue_count = sum(1 for plane in plane_queue if plane is not None)

    queue = queue_count == len(plane_queue)

    if not queue:  # Plane Queue is full
        for plane in plane_queue:
            if plane and plane.has_available_seats():
                return plane
    elif queue:  # Plane queue is not full
        new_plane = Plane(passenger.plane)
