nc = int(input())

for _ in range(nc):
    n,q = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    ansL = a
    lmaxA = 0
    lmaxB = 0
    prefSum = [0]*(n+1)
    for i in range(n-1,-1,-1):
        if a[i]>lmaxA:
            lmaxA = a[i]
        if b[i]>lmaxB:
            lmaxB = b[i]
        ansL[i] = max(lmaxA,lmaxB)

    for i in range(n):
        prefSum[i+1]=prefSum[i]+ansL[i]

    finAns = []
    for j in range(q):
        l,r = map(int, input().rstrip().split())
        finAns.append(prefSum[r]-prefSum[l-1])
    print(*finAns)
