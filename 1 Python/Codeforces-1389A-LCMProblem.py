# 2 versions, both work O(1)
#

#version 2 - one liner
nc = int(input())

for _ in range(nc):
    l,r = map(int, input().rstrip().split())
    print(l,2*l) if r//l>=2 else print(-1,-1)

#version 1 - to show the step by step logic of the one-liner
nc = int(input())

for _ in range(nc):
    l,r = map(int, input().rstrip().split())
    ans = [-1,-1]
    if r%l==0: #the trivial case
        ans = [l,r]
    else:
        if r//l>=2:
            ans = [l,2*l]
    
    print(*ans)
