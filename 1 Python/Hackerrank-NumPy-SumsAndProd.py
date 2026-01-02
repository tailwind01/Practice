import numpy as np

n,m = map(int,input().rstrip().split())

listCollection = []

for _ in range(n):
    iterList = list(map(int, input().rstrip().split()))
    listCollection+=[iterList]

npConvertedList = np.array(listCollection)

sums = np.sum(npConvertedList, axis = 0)

print(np.prod(sums))
