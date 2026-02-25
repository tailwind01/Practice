nc = int(input())

for _ in range(nc):
    n = int(input())
    ans = 1 if n%2 == 0 else 0
    if(n%2==0):
        ans+=n//4
    print(ans)
