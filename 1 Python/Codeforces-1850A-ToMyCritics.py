from itertools import combinations as c
nc = int(input())

for _ in range(nc):
    abc = list(map(int,input().rstrip().split()))
    combs = list(c(abc,2))
    sumArr = 0
    for x in combs:
        if sum(x) >=10:
            sumArr+=1
        else:
            sumArr+=0
    if sumArr>=1:
        print("YES")
    else:
        print("NO")
