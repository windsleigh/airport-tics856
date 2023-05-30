runtime = 1000000
tickets = 100
seats = 100
# Check In
counters = 5
checkin_counters = ["free"] * counters
totems = 5
checkin_totems = ["free"] * totems

# Security
stations = 5
security = ["free"] * stations

# Plane
max_planes = 5
gates = [None] * max_planes

gate_counters = ["free"] * max_planes


checkin = {
    1: "counter",
    2: "totem",
    3: "online",
}
