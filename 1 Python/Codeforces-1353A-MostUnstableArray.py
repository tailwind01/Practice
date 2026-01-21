def usArray(n,x):
    if n==1:
        return 0
    elif n==2:
        return x
    else:
        return 2*x
        
nc = int(input())

for _ in range(nc):
    n,x = map(int, input().rstrip().split())
    print(usArray(n,x))
