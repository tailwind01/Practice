#/tailwind code


nc = int(input())

for _ in range(nc):
    s = int(input())
    ar = list(map(int, input().rstrip().split()))
    mysum = sum(ar)
    initmean = mysum/s
    if mysum>0:
        if initmean>1:
            print(mysum-s)
        elif initmean<1:
            print(1)
        else:
            print(0)
    else:
        print(1)
