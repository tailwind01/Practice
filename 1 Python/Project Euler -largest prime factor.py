#a tailwind code for problem 3 of Project Euler
import math as m
def isprime(n):
    flag = 1
    for i in range(2,m.ceil(pow(n,0.5))+1):
        if n%i==0:
            flag=0
            break
    if flag==0:
        return 0==1
    else:
        return 1==1

num = 600851475143
ce = int(m.sqrt(num))

for j in range(ce+1, 2, -1):
    if num%j==0:
        if isprime(j):
            print(j)
            break

print(isprime(6857))
