nc = int(input())

for _ in range(nc):
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    ctr = 1 # assuming that we can make array whatever we want it to be
    modArr = [x%2 for x in nums]
    set_mArr = set(modArr)
    if len(set_mArr)==2:
        for y in range(1,len(modArr)):
            if modArr[y]==modArr[y-1]:
                ctr = 0
                break

    print("YES" if ctr==1 else "NO")
