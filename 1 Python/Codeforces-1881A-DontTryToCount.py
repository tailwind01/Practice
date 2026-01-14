nc=int(input())

for _ in range(nc):
    a,b = map(int,input().rstrip().split())
    x = str(input())
    y = str(input())
    
    maxIterations = 6 #as n x m is less than 25 (which is betn 4th and 5th powers of 2)
    
    ans = -1
    newX = ""
    
    for i in range(maxIterations):
        newX = (2**i)*x
        if y in newX:
            ans = i
            break
    
    print(ans)
