nc = int(input())


for _ in range(nc):
    n,k = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    sortedA = sorted(a)
    ReverseSortedB = sorted(b)[::-1]

    for x in range(n):
        if k>0 and sortedA[x]<ReverseSortedB[x]:
            sortedA[x]=ReverseSortedB[x]
            k-=1

    print(sum(sortedA))




