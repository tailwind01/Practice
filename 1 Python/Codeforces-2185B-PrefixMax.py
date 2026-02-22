tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(max(arr)*n)
