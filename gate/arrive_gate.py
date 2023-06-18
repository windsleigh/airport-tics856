from config import gates, gate_counters, missed_flights, plane_history
from methods.insert_fel import insert_fel
from objects.event import Event


def arrive_gate(FEL, event):
    global gates, gate_counters, missed_flights
    # Time passenger arrives at gate
    event.entity.time = event.clock

    # Check if the plane has already exited
    if event.entity.plane.id in plane_history:
        # The plane has already exited
        missed_flights += 1
        return

    # Plane is not in gate
    if gates[event.entity.plane.gate] is None:
        # Passenger missed flight
        missed_flight += 1
        return

    if gates[event.entity.plane.gate].status == "arriving":
        event.entity.plane.add_passenger(event.entity)

    if gates[event.entity.plane.gate].status == "boarding":
        # check counter state
        # If counter is free
        if gate_counters[event.entity.plane.gate] == "free":
            # New serve event
            event.entity.server = event.entity.plane.gate
            new_serve_event = Event(event.clock, "ServeGate", event.entity)
            insert_fel(FEL, new_serve_event)
            return
        else:
            # add to queue if not free
            event.entity.plane.add_passenger(event.entity)
