#passed all testcases
#simple pycode by tailwind

import math as m
def isprime(n):
    flag = 1
    for i in range(2,m.ceil(pow(n,0.5))+1):
        if n%i==0:
            flag=0
            break
    if flag==0:
        return 0==1
    else:
        return 1==1

nc = int(input())
for _ in range(nc):
    num = int(input())
    if num==1:
        print("YES")
    elif isprime(num+1):
        print("NO")
    else:
        print("YES")
