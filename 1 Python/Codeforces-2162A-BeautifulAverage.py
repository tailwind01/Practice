nc = int(input())

for _ in range(nc):
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    print(max(nums))
