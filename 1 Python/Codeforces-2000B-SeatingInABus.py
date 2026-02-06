nc = int(input())

for _ in range(nc):
    s = int(input())
    order = list(map(int, input().rstrip().split()))
    adherence = 1
    minSeat = maxSeat = order[0]
    for i in range(1,s):
        currSeat = order[i]
        if currSeat==minSeat-1:
            minSeat = currSeat
        elif currSeat == maxSeat+1:
            maxSeat = currSeat
        else:
            adherence = 0
            break

    print("YES" if adherence==1 else "NO")
