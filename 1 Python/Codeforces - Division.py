t = int(input())

for _ in range(t): 
    commStr = 'Division '
    varStrs = ['1','2','3','4']
    testRating = int(input())
    
    if testRating>=1900:
        print(commStr+varStrs[0])
    elif testRating>=1600:
        print(commStr+varStrs[1])
    elif testRating >= 1400:
        print(commStr+varStrs[2])
    else:
        print(commStr+varStrs[3])

    

