import numpy as np
import matplotlib.pyplot as plt

from objects.passenger import Passenger
from objects.plane import Plane
from objects.event import Event

from methods.time_routine import time_routine

from checkin.arrive_checkin import arrive_checkin
from checkin.exit_checkin import exit_checkin
from checkin.serve_checkin import serve_checkin

from security.arrive_security import arrive_security
from security.exit_security import exit_security
from security.serve_security import serve_security

from gate.arrive_gate import arrive_gate
from gate.exit_gate import exit_gate
from gate.serve_gate import serve_gate

from plane.arrive_plane import arrive_plane
from plane.board_plane import board_plane
from plane.exit_plane import exit_plane

from config import (
    runtime,
    tickets,
    seats,
    counter_queue,
    totem_queue,
    security_queue,
    time_in_airport,
    time_in_counters,
    time_in_totems,
    time_in_security,
    time_in_gate,
    no_seats,
)


def loop():
    # Constants
    global runtime, tickets, seats

    # Variables
    clock = 0

    # Entities
    plane1 = Plane(1, "arriving", tickets - 1, seats, None, None)
    plane2 = Plane(2, "arriving", tickets, seats, None, None)
    plane3 = Plane(3, "arriving", tickets, seats, None, None)
    plane4 = Plane(4, "arriving", tickets, seats, None, None)
    plane5 = Plane(5, "arriving", tickets, seats, None, None)
    plane6 = Plane(6, "arriving", tickets, seats, None, None)
    plane7 = Plane(7, "arriving", tickets, seats, None, None)
    plane8 = Plane(8, "arriving", tickets, seats, None, None)
    plane9 = Plane(9, "arriving", tickets, seats, None, None)
    plane10 = Plane(10, "arriving", tickets, seats, None, None)
    plane11 = Plane(11, "arriving", tickets, seats, None, None)
    plane12 = Plane(12, "arriving", tickets, seats, None, None)
    plane13 = Plane(13, "arriving", tickets, seats, None, None)
    plane14 = Plane(14, "arriving", tickets, seats, None, None)
    plane15 = Plane(15, "arriving", tickets, seats, None, None)
    plane16 = Plane(16, "arriving", tickets, seats, None, None)
    plane17 = Plane(17, "arriving", tickets, seats, None, None)
    plane18 = Plane(18, "arriving", tickets, seats, None, None)
    plane19 = Plane(19, "arriving", tickets, seats, None, None)
    plane20 = Plane(20, "arriving", tickets, seats, None, None)

    passenger = Passenger(0, plane1, "counter", None, None, None, 0)

    # Events
    plane_event1 = Event(0, "ArrivePlane", plane1)
    plane_event2 = Event(0, "ArrivePlane", plane2)
    plane_event3 = Event(0, "ArrivePlane", plane3)
    plane_event4 = Event(0, "ArrivePlane", plane4)
    plane_event5 = Event(0, "ArrivePlane", plane5)
    plane_event6 = Event(0, "ArrivePlane", plane6)
    plane_event7 = Event(0, "ArrivePlane", plane7)
    plane_event8 = Event(0, "ArrivePlane", plane8)
    plane_event9 = Event(0, "ArrivePlane", plane9)
    plane_event10 = Event(0, "ArrivePlane", plane10)
    plane_event11 = Event(0, "ArrivePlane", plane11)
    plane_event12 = Event(0, "ArrivePlane", plane12)
    plane_event13 = Event(0, "ArrivePlane", plane13)
    plane_event14 = Event(0, "ArrivePlane", plane14)
    plane_event15 = Event(0, "ArrivePlane", plane15)
    plane_event16 = Event(0, "ArrivePlane", plane16)
    plane_event17 = Event(0, "ArrivePlane", plane17)
    plane_event18 = Event(0, "ArrivePlane", plane18)
    plane_event19 = Event(0, "ArrivePlane", plane19)
    plane_event20 = Event(0, "ArrivePlane", plane20)

    passenger_event = Event(0, "ArriveCheckIn", passenger)

    # Future Event List
    FEL = [
        plane_event1,
        plane_event2,
        plane_event3,
        plane_event4,
        plane_event5,
        plane_event6,
        plane_event7,
        plane_event8,
        plane_event9,
        plane_event10,
        plane_event11,
        plane_event12,
        plane_event13,
        plane_event14,
        plane_event15,
        plane_event16,
        plane_event17,
        plane_event18,
        plane_event19,
        plane_event20,
        passenger_event,
    ]
    # Define header
    header = f'{"Metric":<25} | {"Average Time (minutes)":<25}'
    separator = "-" * len(header)
    while runtime > 0:
        # print("totem queue", len(totem_queue))
        # print("counter queue", len(counter_queue))
        # print("security queue", len(security_queue))
        event, clock = time_routine(FEL, clock)
        match event.kind:
            # Check In routines
            case "ArriveCheckIn":
                arrive_checkin(FEL, event)
            case "ServeCheckIn":
                serve_checkin(FEL, event)
            case "ExitCheckIn":
                exit_checkin(FEL, event)

            # Security routines
            case "ArriveSecurity":
                arrive_security(FEL, event)
            case "ServeSecurity":
                serve_security(FEL, event)
            case "ExitSecurity":
                exit_security(FEL, event)

            # Gate routines
            case "ArriveGate":
                arrive_gate(FEL, event)
            case "ServeGate":
                serve_gate(FEL, event)
            case "ExitGate":
                exit_gate(FEL, event)

            # Plane routines
            case "ArrivePlane":
                arrive_plane(FEL, event)
            case "BoardPlane":
                board_plane(FEL, event)
            case "ExitPlane":
                exit_plane(FEL, event)
        plane_id_info = ""

        if hasattr(event.entity, "plane") and event.entity.plane:
            plane_id_info = f" | Plane ID: {event.entity.plane.id}"

        print(
            f"Clock: {clock:.2f} | Entity ID: {event.entity.id}{plane_id_info} | Queue Lengths | Totem Queue: {len(totem_queue)} | Counter Queue: {len(counter_queue)} | Security Queue: {len(security_queue)}"
        )
        print(separator)
        runtime -= 1

    # Assuming you already have the values calculated
    average_time_in_airport = np.mean(time_in_airport)
    average_time_in_counters = np.mean(time_in_counters)
    average_time_in_totems = np.mean(time_in_totems)
    average_time_in_security = np.mean(time_in_security)
    average_time_in_gate = np.mean(time_in_gate)

    # Define rows
    rows = [
        f'{"Time in airport":<25} | {average_time_in_airport:<25.2f}',
        f'{"Time in counters":<25} | {average_time_in_counters:<25.2f}',
        f'{"Time in totems":<25} | {average_time_in_totems:<25.2f}',
        f'{"Time in security":<25} | {average_time_in_security:<25.2f}',
        f'{"Time in gate":<25} | {average_time_in_gate:<25.2f}',
    ]

    # Print table
    print(separator)
    print(header)
    print(separator)
    for row in rows:
        print(row)
    print(separator)

    # Plotting the time values
    plt.plot(time_in_totems, label="Time in Totems")
    plt.plot(time_in_counters, label="Time in Counters")
    plt.plot(time_in_security, label="Time in Security")
    plt.plot(time_in_gate, label="Time in Gate")
    plt.plot(time_in_airport, label="Time in Airport")

    # Adding labels and title
    plt.xlabel("Iterations")
    plt.ylabel("Time")
    plt.title("Time Spent in Different Sections of the Airport")
    plt.legend()

    # Display the plot
    plt.show()
    return
