import numpy as np

n,m = map(int, input().rstrip().split())

masterList = []

for _ in range(n):
    iterList = list(map(int, input().rstrip().split()))
    masterList+=[iterList]

npArray = np.array(masterList)

print(np.mean(npArray,axis = 1))
print(np.var(npArray,axis=0))
print(round(np.std(npArray,axis=None),11))
