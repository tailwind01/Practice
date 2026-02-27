nc = int(input())

for _ in range(nc):
    size = int(input())
    nums = list(map(int, input().rstrip().split()))
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    ans = 0
    for val in counts.values():
        ans += val // 2
    print(ans)
