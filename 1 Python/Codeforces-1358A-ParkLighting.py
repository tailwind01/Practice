nc = int(input())

for _ in range(nc):
    n,m = map(int,input().rstrip().split())
    print((n*m+1)//2)
