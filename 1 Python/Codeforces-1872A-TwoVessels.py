import math as m
nc = int(input())

for _ in range(nc):
    a,b,c = map(int,input().rstrip().split())
    print(m.ceil(abs(a-b)/(2*c)))
