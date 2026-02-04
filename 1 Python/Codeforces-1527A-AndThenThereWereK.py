import math as m

nc = int(input())

for _ in range(nc):
    n = int(input())
    l2_int = int(m.log2(n))
    ans = pow(2,l2_int)-1
    print(ans)
