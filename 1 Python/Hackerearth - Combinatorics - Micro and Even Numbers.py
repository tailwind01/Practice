#/a tailwind publication
from itertools import combinations as c
n,k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
clist = list(c(arr,k))
flist=[]
for i in clist:
    flag = 0
    for j in i:
        if j%2==0:
            flag=1
            continue
        else:
            flag=0
            break
    flist+=[flag]
    
print(flist.count(1))
