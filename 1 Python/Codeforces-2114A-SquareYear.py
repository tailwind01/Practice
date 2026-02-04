import math as m

t = int(input())

for _ in range(t):
    year = int(input())
    
    if m.sqrt(year)==m.sqrt(year)//1:
        ansL = [0,int(m.sqrt(year))]
    else:
        ansL = [-1]
    
    print(*ansL)
