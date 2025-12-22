#!/bin/python3

import sys
def isprime(n):
    if n==1:
        return 1==2
    elif n==2:
        return 1==1
    else:
        flag = 1
        for i in range(2,int(pow(n,0.5))+1):
           if n%i==0:
               flag = 0
               break
        if flag==1:
            return 1==1
        else:
            return 0==1

maxnum = 1000000
primes = []
i = 1
while(i<maxnum):
    if isprime(i):
        primes+=[i]
    i+=1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])
