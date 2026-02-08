nc = int(input())

for _ in range(nc):
    n,a,b,c = map(int, input().rstrip().split())
    fullSets = (n//(a+b+c))*3
    lastChunk = n%(a+b+c)
    days = fullSets
    iterNum = 1
    while lastChunk>0:
        if iterNum==1:
            dist = a
        elif iterNum == 2:
            dist = b
        else:
            dist = c
        lastChunk-=dist
        iterNum+=1
        days+=1
    print(days)
