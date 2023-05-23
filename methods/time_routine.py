def time_routine(FEL, clock):
    event = FEL[0]
    FEL.pop(0)
    clock = event.clock
    return event
