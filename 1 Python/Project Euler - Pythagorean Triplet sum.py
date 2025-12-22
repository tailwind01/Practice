# a tailwind pub
import math as m
triples = []
for i in range(1,1001):
    for j in range(i+1,1001):
        calc = pow(i,2)+pow(j,2)
        if pow(calc, 0.5) in range(j,1001):
            triples+=[[i,j,int(pow(calc,0.5))]]
reltriple = []
for t in triples[::-1]:
    if sum(t)==1000:
        reltriple+=[t]
        break

print(m.prod(reltriple[0])) #since reltriple is a 2d list
