def insert_event_in_FEL(FEL, event):
    for i in range(len(FEL)):
        if FEL[i][1] > event[1]:
            FEL.insert(i, event)
            return
    FEL.append(event)
