nc = int(input())
for _ in range(nc):
    size = int(input())
    inp = list(map(int,input().rstrip().split())) 
    oddHalf = []
    evenHalf = []
    
    if size%2==0:
        for i in range(size):
            if i<size//2:
                oddHalf.append(inp[i])
            else:
                evenHalf.append(inp[i])
    else:
        for i in range(size):
            if i<=size//2:
                oddHalf.append(inp[i])
            else:
                evenHalf.append(inp[i])
    
    origInEven = evenHalf[::-1]
    
    ansList = []
    
    for x in range(size):
        if x%2==0:
            ansList.append(oddHalf[x//2])
        else:
            ansList.append(origInEven[x//2])
            
    print(*ansList)
