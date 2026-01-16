nc = int(input())

for _ in range(nc):
    size = int(input())
    givenArr = list(map(int,input().rstrip().split()))
    set_arr = set(givenArr) #to find Unique Elements in array
    
    if len(set_arr)!=1:
        sortedArr = sorted(givenArr)
        #after sorting, we can meet the condition in a sense that the largest number wont be the divisor of any numbers preceding it!
        sub_arr1 = []
        sub_arr2 = []
        for e in sortedArr:
            if e!=sortedArr[-1]:
                sub_arr1.append(e)
            elif e==max(sortedArr):
                sub_arr2.append(e)
            else:
                continue
           
        print(len(sub_arr1), len(sub_arr2))
        print(*sub_arr1)
        print(*sub_arr2)
    else:
        print(-1)
