nc = int(input())

for _ in range(nc):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    opers = 0
    for i in range(n):
        diff = a[i]-b[i]
        if diff>0:
            opers+=diff
    print(opers+1)
