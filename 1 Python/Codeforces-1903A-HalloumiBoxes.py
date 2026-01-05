nc = int(input())

for _ in range(nc):
    n,k = map(int, input().rstrip().split())
    currArr = list(map(int, input().rstrip().split()))
    
    #the only case to solve for is the case where k<=1 and we have to decide whether the array is in non decreasing order or not
    
    if k<=1:
        counter = 1
        for x in range(1,n):
            if currArr[x]<currArr[x-1]:
                counter = 0
                break
        if counter == 1:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
