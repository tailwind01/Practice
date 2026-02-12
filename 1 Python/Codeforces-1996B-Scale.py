nc = int(input())

for _ in range(nc):
    n,k = map(int, input().rstrip().split())
    inps = []
    for i in range(n):
        currL = str(input())
        inps.append(currL)

    ansL = []

    i = 0
    while(i<n):
        take = inps[i]
        comp = ""
        for j in range(1,len(take)+1,1):
            if j%k==0:
                comp+=take[j-1]
        ansL.append(comp)
        i+=k

    print("\n".join(ansL))
