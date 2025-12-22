t = int(input())

for _ in range(t):
    l = int(input())
    nums = list(map(int, input().split()))
    nums_set = list(set(nums))
    if nums.count(nums_set[0])>1:
        print (nums.index(nums_set[1])+1)
    else:
        print (nums.index(nums_set[0])+1)
