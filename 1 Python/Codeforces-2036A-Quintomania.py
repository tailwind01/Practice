nc = int(input())

for _ in range(nc):
    notes = int(input())
    nums = list(map(int, input().rstrip().split()))
    perfects = [5,7]
    isperfect = 1
    for n in range(1,notes):
        if abs(nums[n]-nums[n-1]) not in perfects:
            isperfect = 0
            break

    print("YES" if isperfect == 1 else "NO")
