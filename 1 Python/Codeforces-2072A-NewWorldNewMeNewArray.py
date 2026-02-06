import math as m
nc = int(input())

for _ in range(nc):
    n,k,p = map(int, input().rstrip().split())
    opersAllowed = m.ceil(abs(k)/p)
    print(opersAllowed if opersAllowed<=n else -1)
