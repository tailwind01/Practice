#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    inpstr = str(num)
    sl = len(inpstr)
    maxprod = 1
    for lm in range(k):
        maxprod*=int(inpstr[lm])
    
    for i in range(sl-k):
        stepprod = 1
        for j in range(i,i+k):
            num = inpstr[j]
            stepprod*=int(num)
        if stepprod>maxprod:
            maxprod=stepprod
    print(maxprod)
