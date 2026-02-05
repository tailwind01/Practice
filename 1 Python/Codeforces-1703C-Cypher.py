# there are 3 versions of the same logic
# my approach with v1 was to find the first principles validation
# once that was validated, I have merged various stages at the input collection itself

#v3 - refined v2
nc = int(input())

for _ in range(nc):
    w = int(input())
    tp = list(map(int, input().rstrip().split()))
    ansArr = []
    for x in range(w):
        nm,mt = map(str, input().rstrip().split())
        # nm is useless..
        netSum = mt.count('D')-mt.count('U')
        ansArr.append((tp[x]+netSum)%10) # we correct for overflow/underflow
    print(*ansArr)

#v2 - refined v1
nc = int(input())

for _ in range(nc):
    w = int(input())
    tp = list(map(int, input().rstrip().split()))
    ansArr = []
    for x in range(w):
        nm,mt = map(str, input().rstrip().split())
        # nm is useless..
        netSum = 0
        for m in mt:
            if m=="U":
                netSum-=1
            else:
                netSum+=1
        ansArr.append((tp[x]+netSum)%10) # we correct for overflow/underflow
    print(*ansArr)

#v1 - the First Principles approach so that the code could be audited if it had bugs
nc = int(input())

for _ in range(nc):
    w = int(input())
    tp = list(map(int, input().rstrip().split()))
    nmoves = []
    moveNetSum = []
    for x in range(w):
        nm,mt = map(str, input().rstrip().split())
        nmoves.append(int(nm))
        netSum = 0
        for m in mt:
            if m=="U":
                netSum-=1
            else:
                netSum+=1
        moveNetSum.append(netSum)
    ansArr = []
    for y in range(w):
        ansArr.append(abs((tp[y]+moveNetSum[y])%10)) # we correct for overflow/underflow
    print(*ansArr)

