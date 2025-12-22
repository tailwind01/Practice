#/tailwind
from math import gcd as g

n = int(input())
totient = [i for i in range(1,n) if g(i,n)==1]
print(len(totient))
