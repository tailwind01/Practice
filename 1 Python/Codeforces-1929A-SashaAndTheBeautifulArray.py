nc = int(input())

for _ in range(nc):
    d = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(max(arr)-min(arr))
