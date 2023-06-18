runtime = 100000
tickets = 100
seats = 100

counter_queue = []
totem_queue = []
security_queue = []

# Check In
counters = 2
checkin_counters = ["free"] * counters
totems = 1
checkin_totems = ["free"] * totems

# Security
stations = 2
security = ["free"] * stations

# Plane
max_planes = 20
gates = [None] * max_planes

gate_counters = ["free"] * max_planes

checkin = {
    1: "counter",  # 5%
    2: "totem",  # 30%
    3: "online",  # 65%
}

time_in_totems = []
time_in_counters = []
time_in_security = []
time_in_gate = []
time_in_airport = []

plane_history = []

missed_flights = 0
