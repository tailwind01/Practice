import numpy as np

n,m = map(int,input().rstrip().split())
masterInput = []

for _ in range(n):
    currList = list(map(int, input().rstrip().split()))
    masterInput+=[currList]

np_operated = np.array(masterInput)

print(np.transpose(np_operated))
