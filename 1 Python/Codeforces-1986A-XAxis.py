nc = int(input())

for _ in range(nc):
    currNums = list(map(int, input().rstrip().split()))
    asSet = sorted(set(currNums)) #we sort at set stage itself and then we can traverse
    #trivial cases : length of set==1 or 2
    ans = 0 #for trivial case where x1,x2,x3 are all equal (so length of set ==1)
    if len(asSet)==2:
        ans = asSet[1]-asSet[0]
    elif len(asSet)==3:
        ans = asSet[2]-asSet[0]

    print(ans)
