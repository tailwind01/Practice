nc=int(input())

for _ in range(nc):
    a,b,c = map(str, input().rstrip().split())
    print(a[0]+b[0]+c[0])
