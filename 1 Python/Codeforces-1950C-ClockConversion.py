from datetime import datetime as dt
nc = int(input())

for _ in range(nc):
    inpt = dt.strptime(str(input()),"%H:%M")
    print(inpt.strftime("%I:%M %p"))
