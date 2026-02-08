nc = int(input())

for _ in range(nc):
    a,b = map(int, input().rstrip().split())
    if a==0:
        print (1)
    else:
        print(a+2*b+1)
