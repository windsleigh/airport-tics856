runtime = 1000
tickets = 100
seats = 100

counter_queue = []
totem_queue = []
security_queue = []

# Check In
counters = 10
checkin_counters = ["free"] * counters
totems = 10
checkin_totems = ["free"] * totems

# Security
stations = 15
security = ["free"] * stations

# Plane
max_planes = 20
gates = [None] * max_planes

gate_counters = ["free"] * max_planes


time_in_totems = []
time_in_counters = []
time_in_security = []
time_in_gate = []
time_in_airport = []

plane_history = {}

missed_flights = 0
no_seats = 0
