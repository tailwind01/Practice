#!/bin/python3

import math
import os
import random
import re
import sys

def larrysArray(A):
    parity  = 0
    for i in range(0,len(A)-1):
        for j in range(i,len(A)):
            if (A[i]>A[j]):
                parity+=1
    
    if parity%2==0: return "YES"  
    else: return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()

