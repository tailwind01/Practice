nc = int(input())

for _ in range(nc):
    n = int(input())
    init = str(input())
    finish = str(input())
    iCt = init.count('1')
    fCt = finish.count('1')
    days = 0
    for i in range(n):
        istate = init[i]
        fstate = finish[i]
        if fstate=='1' and istate=='0':
            days+=1
    print(days-min(fCt-iCt,0)) # to correct for the finished cats provided from init cats
