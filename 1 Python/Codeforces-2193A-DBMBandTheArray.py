tc = int(input())

for _ in range(tc):
    n,s,x = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    ans = "Yes" if (s>=sum(nums) and (s-sum(nums))%x==0) else "No"
    print(ans)
