n = int(input())
#let's hypothesize the problem to be the following
#adjacent switches are possible only if n is even
#perfection will be achieved only if we can switch in adjacent elements (so the total size has to be even?)
#so the output would be a list like 2 1 4 3 6 5 etc

if n%2==0:
    ans = []
    for j in range(1,n+1):
        if j%2==0:
            ans.append(j-1)
        else:
            ans.append(j+1)
    
    print(*ans)
else:
    print(-1)
