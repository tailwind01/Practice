import math as m
nc = int(input())

for _ in range(nc):
    n = int(input())
    a = list(map(int, input().split()))
    minElem = min(a)
    a[a.index(minElem)]=minElem+1 #bottleneck fixed
    print(m.prod(a))
