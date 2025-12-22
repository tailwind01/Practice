#/ easy solution, runtime 61ms, memory 0Kb
nc = int(input())
for _ in range(nc):
    n,x = map(int, input().rstrip().split())
    first_floor = [1,2]
    #first floor is constructed
    bal_apts = n-2
    if n in first_floor:
        print(1)
    else:
        if bal_apts%x==0:
            floor = bal_apts//x
        else:
            floor = bal_apts//x +1
        print(floor+1) #because we want floor, not index
