nc = int(input())

for _ in range(nc):
    n = int(input())
    nums = list(map(int,input().rstrip().split()))
    m1ct = nums.count(-1)
    zeroct = nums.count(0)
    ans = zeroct
    if m1ct%2!=0:
        ans+=2
    print(ans)
