#Codeforces 1367B solution

def parityCheck(arr):
    indexCollection = []
    for i in range(len(arr)):
        if (arr[i]%2) != (i%2):
            indexCollection.append([arr[i],i])
    return indexCollection

nc = int(input())

for _ in range(nc):
    arrLen = int(input())
    givenArr = list(map(int, input().rstrip().split()))
    nonEvens = parityCheck(givenArr)
    
    # now we have to check if a swap can be performed such that parity could be achieved
    
    oddNumbers = 0
    evenNumbers = 0
    
    for t in nonEvens:
        if t[0]%2==0:
            evenNumbers+=1
        else:
            oddNumbers+=1
    
    if evenNumbers==oddNumbers: #swaps can be performed if there are enough elements only
        print(evenNumbers)
    else:
        print(-1)
