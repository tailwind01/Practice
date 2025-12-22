#/tailwind code
n = 2
ar=[0,2]
while(n<4000000):
    n = 4*ar[-1]+ar[-2]
    ar+=[n]

print(sum(ar[:-1]))
