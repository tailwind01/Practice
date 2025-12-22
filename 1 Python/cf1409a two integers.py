# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:54:46 2021

@author: tailwind
"""
nc = int(input())
for _ in range(nc):
    a,b = map(int, input().rstrip().split())
    absDiff = abs(a-b)
    if absDiff==0:
        print(0)
    if absDiff<10:
        print(1)
    elif absDiff%10!=0:
        print(absDiff//10 + 1)
    else:
        print(absDiff//10)

