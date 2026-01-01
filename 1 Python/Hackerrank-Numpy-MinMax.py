import numpy as np

n,m = map(int, input().rstrip().split())

array=[]

for _ in range(n):
    phArr = list(map(int, input().rstrip().split()))
    array+=[phArr]

print(max(np.min(array, axis=1)))
