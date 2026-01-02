import numpy as np

inpList = list(map(int,input().rstrip().split()))

np_array = np.array(inpList) 

print(np.reshape(np_array, (3,3))) #to make reshape into 3x3
