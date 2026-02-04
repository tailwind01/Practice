nc = int(input())

for _ in range(nc):
    l =  int(input())
    iL = list(map(int, input().rstrip().split()))
    corrs = 0

    for i in range(l-1):
        if iL[i]%2==iL[i+1]%2:
            corrs+=1

    print(corrs)
