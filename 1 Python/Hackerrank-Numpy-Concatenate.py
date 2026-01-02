import numpy as np

n,m,p = map(int, input().rstrip().split())
nList = []
mList = []

for x in range(n+m):
    if x < n:
        iterList = list(map(int, input().rstrip().split()))
        nList+=[iterList]
    else:
        iterList = list(map(int, input().rstrip().split()))
        mList+=[iterList]

nL_as_npArr = np.array(nList)
mL_as_npArr = np.array(mList)

print (np.concatenate((nL_as_npArr,mL_as_npArr), axis=0))
