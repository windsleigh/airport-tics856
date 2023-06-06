from config import total_airport_time

def total_time(event):
    global total_airport_time
    final_time=event.clock
    arrival_time=event.entity.arrival_time
    total_airport_time.append(final_time-arrival_time)