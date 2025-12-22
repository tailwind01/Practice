#/tailwind code, 77 ms, 0 Kb
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

#a,d for first, b,c,d for second
cost = 0
if e>=f:
    cost+=min(a,d)*e
    d-=min(a,d)
    cost+=min(b,c,d)*f
else:
    cost+=min(b,c,d)*f
    d-=min(b,c,d)
    cost+=min(a,d)*e
    
print(cost)
    
