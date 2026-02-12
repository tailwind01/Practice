nc = int(input())

for _ in range(nc):
    n,x = map(int, input().rstrip().split())
    doors = list(map(int, input().rstrip().split()))
    oneIndices = [i+1 for i in range(len(doors)) if doors[i]==1]
    print("Yes" if (oneIndices[-1]-oneIndices[0])<x else "No")
