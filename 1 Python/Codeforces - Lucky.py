t = int(input())

for _ in range(t): 
    x = str(input())
    firstHalfsum = 0
    secondHalfsum = 0
    firstList  = x[:3]
    secondList = x[3:]
    for i in firstList:
        firstHalfsum+=int(i)
    for j in secondList:
        secondHalfsum+=int(j)
        
    if firstHalfsum==secondHalfsum:
        print("YES")
    else:
        print("NO")

    

