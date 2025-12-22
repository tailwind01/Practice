#/a tailwind code/
import math
nc = int(input())

for _ in range(nc):
    s = int(input())
    ar = list(map(int, input().rstrip().split()))
    mysum = sum(ar)
    initmean = mysum/s
    print(math.ceil(initmean))
