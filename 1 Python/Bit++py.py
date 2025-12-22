# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:05:10 2021

@author: sai
"""


n_testcases = int(input())

count = 0
for i in range(n_testcases):
    strin = str(input())
    if(strin=='X++' or strin =='++X' or strin=='+X+'):
        count+=1
    else:
        count-=1
print(count)