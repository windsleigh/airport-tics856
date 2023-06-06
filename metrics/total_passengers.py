from config import total_passengers_in

def passengers_in(event):
    total_passengers_in.append(event.entity.tickets - event.entity.seats)
