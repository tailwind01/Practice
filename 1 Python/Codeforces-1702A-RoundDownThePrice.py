import math as m
nc = int(input())

for _ in range(nc):
    price = int(input())
    n10p = int(m.log10(price))
    ans = price-pow(10,n10p)
    print(ans)
