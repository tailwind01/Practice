nc = int(input())

for _ in range(nc):
    n = int(input())
    toColour = sorted(list(map(int, input().rstrip().split())))
    if len(toColour)>2:
        mpt = (len(toColour)+1)//2
        ans = (sum(toColour[mpt:])-sum(toColour[:mpt]))
        if (len(toColour)%2!=0):
            ans+=toColour[mpt-1] # as python works zero-indexed, bug corrected
        print(ans)
    elif len(toColour)==2:
        print((toColour[-1]-toColour[0]))
    else:
        print(0)
