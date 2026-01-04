nc = int(input())

for _ in range(nc):
    l,a,b = map(int, input().rstrip().split())
    maxNumPossible = 0
    for i in range(l):
        if (a+i*b)%l > maxNumPossible:
            maxNumPossible = (a+i*b)%l
    print(maxNumPossible)
