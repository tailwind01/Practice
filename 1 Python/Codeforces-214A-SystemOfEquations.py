import math

n,m = map(int, input().rstrip().split())

top = int(math.sqrt(max(n,m)))+2

ansArr=[]

for i in range(top):
    for j in range(top):
        if (pow(i,2)+j)==n and (pow(j,2)+i)==m:
            ansArr+=[[i,j]]

print(len(ansArr))
