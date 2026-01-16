nc = int(input())

for _ in range(nc):
    n,k = map(int, input().rstrip().split())
    
    if n%k!=0:
        print(1)
        print(n)
    else:
        print(2)
        print(str(n+1),str(-1))
