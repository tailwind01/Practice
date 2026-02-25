import math as m
nc = int(input())

for _ in range(nc):
    n = int(input())
    ans = 2 if n==1 else m.ceil(n/3)
    print(ans)
