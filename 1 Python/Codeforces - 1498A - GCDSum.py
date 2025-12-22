#/tailwind code, runtime 295ms
from math import gcd as g
nc = int(input())

for _ in range(nc):
    base = int(input())
    
    for i in range(base, base+100001):
        asstr = str(i)
        digisum = 0
        for s in asstr:
            digisum+=int(s)
        if g(i,digisum)>1:
            print(i)
            break
