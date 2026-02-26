import math as m
nc = int(input())

for _ in range(nc):
    n = int(input())
    # having middle one to be lowest possible means having first one largest (second place winner) possible
    second = m.ceil(n/3)
    first = second+1 
    third = n-first-second
    # arithmetic correction to have sanity
    if third==0:
        third+=1
        second-=1
    ans = [second, first,third]
    print(*ans)
