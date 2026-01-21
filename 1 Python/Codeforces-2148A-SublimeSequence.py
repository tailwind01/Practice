nc = int(input())

for _ in range(nc):
    x,n = map(int, input().rstrip().split())
    if n%2==0:
        print(0)
    else:
        print(x)
