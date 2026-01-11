
nc = int(input())

for _ in range(nc):
    n = int(input())
    a = list(map(int, input().split()))
    setA = set(a)
    
    print("Yes" if len(setA)==n else "No")
