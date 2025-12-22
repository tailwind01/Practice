reqL = [6,2,5,5,4,5,6,3,7,6]
nc = int(input())

for _ in range(nc):
    a,b = map(int, input().rstrip().split())
    numstr = str(a+b)
    mcount = 0
    
    for d in numstr:
        mcount+=reqL[int(d)]
    
    print(mcount)
