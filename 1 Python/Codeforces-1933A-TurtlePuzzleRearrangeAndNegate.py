nc = int(input())

for _ in range(nc):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    runningSum=0
    for x in l:
        runningSum+=abs(x)
    print(runningSum)
