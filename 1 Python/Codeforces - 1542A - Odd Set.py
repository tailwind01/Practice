#/tailwind code, 62ms
nc = int(input())

for _ in range(nc):
    n = int(input())
    mylist = list(map(int, input().rstrip().split()))
    numOdd = 0
    numEven = 0

    for i in mylist:
        if i%2==0:
            numEven+=1
        else:
            numOdd+=1
    if numEven == numOdd and numEven==n:
        print("Yes")
    else:
        print("No")
        
 
