nc = int(input())

for _ in range(nc):
    s = int(input())
    arr = list(map(int, input().rstrip().split()))
    sortedArr = sorted(arr)
    
    if arr==sortedArr: 
        minDiff = max(sortedArr) # to calculate minimum adjacent difference
        itla = s-1
        for e in range(len(sortedArr)-1):
            if sortedArr[e]!=sortedArr[e+1]:
                if abs(sortedArr[e]-sortedArr[e+1])<minDiff:
                    minDiff = abs(sortedArr[e]-sortedArr[e+1])
                    itla = e
        subArr = [sortedArr[e-1],sortedArr[e],sortedArr[e+1]]
        diffArr = [abs(sortedArr[e-1]-sortedArr[e]), abs(sortedArr[e]-sortedArr[e+1])]
        
        if 0 in diffArr and len(sortedArr)<=3:
            print(1)
        else:
            print(minDiff//2 + 1) 
    
    else:
        print(0)
