#https://www.hackerrank.com/challenges/anagram/problem


import math
import os
import random
import re
import sys

def anagram(s):
    if len(s)%2!=0:
        return -1
    else:
        mp = len(s)//2
        s1 = s[:mp]
        s2 = s[mp:]
        ct = mp #initialised at midpoint, if repetitions, can delete
        collected = []
        for l in s1:
            if l in s2:
                if l not in collected:
                    collected+=[l]
                    minct = min(s1.count(l), s2.count(l))
                    ct-=minct
        return ct
                
nc = int(input())
ansAr=[]
for _ in range(nc):
    s = str(input())
    ansAr+=[str(anagram(s))]

print("\n".join(ansAr))
