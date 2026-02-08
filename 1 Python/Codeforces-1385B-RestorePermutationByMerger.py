nc = int(input())

for _ in range(nc):
    n = int(input())
    merged = list(map(int, input().rstrip().split()))
    s_merged = list(dict.fromkeys(merged))
    print(*s_merged)
