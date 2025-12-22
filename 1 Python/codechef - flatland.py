#/published by tailwind, runtime 0.02s, memory 17.5m


def numcircles(n):
    ct = 0
    while(pow(n,0.5)!=int(pow(n,0.5))):
        n -= int(pow(n,0.5))**2
        ct+=1
    else:
        ct+=1
    return ct

nc = int(input())
for _ in range(nc):
    n= int(input())
    print(numcircles(n))

