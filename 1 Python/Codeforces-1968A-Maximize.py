import math as m

nc = int(input())

for _ in range(nc):
    x = int(input())
    compareNum = 0
    tentY = 1
    for y in range(2,x,1):
        computed = m.gcd(y,x)+y
        if computed>compareNum:
            tentY = y
            compareNum = computed
    
    print(tentY)
