from config import gates, gate_counters
from methods.insert_fel import insert_fel
from objects.event import Event


def arrive_gate(FEL, event):
    global gates, gate_counters
    print("arrive gate----------------------------")

    # Time passenger arrives at gate
    event.entity.time = event.clock
    print("plane status: ", gates[event.entity.plane.gate].status)
    if gates[event.entity.plane.gate].status == "arriving":
        event.entity.plane.add_passenger(event.entity)
        print("arriving----------------------------")

    if gates[event.entity.plane.gate].status == "boarding":
        print("boarding----------------------------")

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
    if gates[event.entity.plane.gate].status == "leaving":
        # Passenger missed the flight
        print("leaving----------------------------")

        pass
