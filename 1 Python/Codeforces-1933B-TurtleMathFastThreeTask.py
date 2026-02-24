#refined after AC
nc = int(input())
for _ in range(nc):
    e = int(input())
    nums = list(map(int, input().rstrip().split()))
    ctof1s = sum([n%3==1 for n in nums])
    total = sum(nums)
    ans = 0 if total%3==0 else 1
    # the real problematic scenario is only when total mod 2 == 1 and count of 1s is 0
    if total%3==1:
        if ctof1s==0:
            ans+=1
    print(ans)

#crude version of the code
nc = int(input())

for _ in range(nc):
    e = int(input())
    nums = list(map(int, input().rstrip().split()))
    indMods = [n%3 for n in nums]
    ctof1s = indMods.count(1)
    ctof2s = indMods.count(2)
    total = sum(nums)
    ans = 0 if total%3==0 else 1
    # the real problematic scenario is only when total mod 2 == 1 and count of 1s is 0
    if total%3==1:
        if ctof1s==0:
            ans+=1
    print(ans)
