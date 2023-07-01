from config import time_in_airport


def total_time(event):
    final_time = event.clock
    arrival_time = event.entity.arrival_time
    total_time = final_time - arrival_time
    time_in_airport[final_time] = total_time
    return
