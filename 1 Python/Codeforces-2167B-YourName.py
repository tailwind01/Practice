#v2 parsimonious
from collections import Counter as ctr
nc = int(input())

for _ in range(nc):
    size = int(input())
    a,b = map(str, input().rstrip().split())
    actr = ctr(a)
    bctr = ctr(b)
   
    print("Yes" if actr==bctr else "No")


#v1 verbose solution

from collections import Counter as ctr
nc = int(input())

for _ in range(nc):
    size = int(input())
    a,b = map(str, input().rstrip().split())
    actr = ctr(a)
    bctr = ctr(b)
    compList = []
    for element,count in bctr.items():
        compList.append(actr[element]-count)
    
    flag = 1

    for e in compList:
        if e!=0:
            flag = 0
            break
    
    print("Yes" if flag==1 else "No")
