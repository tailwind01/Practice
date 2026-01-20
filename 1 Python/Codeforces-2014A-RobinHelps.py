nc = int(input())

for _ in range(nc):
    n,k = map(int, input().rstrip().split())
    gArr = list(map(int, input().rstrip().split()))
    stock = 0
    ans = 0
    for i in range(n):
        if gArr[i]==0 and stock>0:
            stock-=1
            ans+=1
        if gArr[i]>=k:
            stock+= gArr[i]
    
    print(ans)
