nc = int(input())

for _ in range(nc):
    sides = list(map(int,input().rstrip().split()))
    sides_asSet = set(sides)
    
    print("Yes" if len(sides_asSet)==1 else "No")
