
nc = int(input())

for _ in range(nc):
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))
