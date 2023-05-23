# Runtime
runtime = 50

# Plane Capacity
seats = 100

# Gates
gates = 5
board_gates = [] * gates

# Evil array creation
gates_queues = [[] for _ in range(gates)]
# gates_counter = [[] for _ in range(gates)]

total_planes_queue = 5
plane_queue = [False] * total_planes_queue

# Check In
counters = 5
checkin_counters = ["free"] * counters
totems = 5
checkin_totems = ["free"] * totems

# Security
stations = 5
security = ["free"] * stations

# Boarding


# Dictionaries

kind = {
    1: "ArriveCheckIn",
    2: "ServeCheckIn",
    3: "ExitCheckIn",
    4: "ArriveSecurity",
    5: "ServeSecurity",
    6: "ExitSecurity",
    7: "ArriveBoarding",
    8: "ServeBoarding",
    9: "ExitBoarding",
    10: "ArrivePlane",
    11: "BoardPlane",
    12: "ExitPlane",
}

checkin = {
    1: "counter",
    2: "totem",
    3: "online",
}
