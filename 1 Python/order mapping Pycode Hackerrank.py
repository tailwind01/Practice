##https://www.hackerrank.com/challenges/jim-and-the-orders/problem

import math
import os
import random
import re
import sys
from operator import itemgetter as ig
n = int(input().strip())
orders = []
for _ in range(n):  
    orders.append(list(map(int, input().rstrip().split())))  
prepT = []
custom = []
for i in range(len(orders)):
    prepped = sum(orders[i])
    prepT+=[prepped]
    custom += [i+1]
    
ans1 = []
for i in range(len(prepT)):
    ans1+=[[prepT[i], custom[i]]] 
ans1.sort(key=ig(0))
ansAr=[]
for i in ans1:
    ansAr+=[str(i[1])]

print(" ".join(ansAr))
