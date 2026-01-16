nc = int(input())

for _ in range(nc):
    size = int(input())
    arr = list(map(int, input().rstrip().split()))
    inSort = sorted(arr)
    
    if arr==inSort: #if already in sorted condition, we can guess the array to be the one given
        print(size)
        print (" ".join(str(x) for x in arr))
    
    else:
        possibAns = [arr[0]] #as condition is less than or equal to..
        for x in range(1, size):
            possibAns.append(arr[x])
            if arr[x]<arr[x-1]: #once more if there is a shortage due to order change
                possibAns.append(arr[x])
        
        print(len(possibAns))
        print(" ".join(str(y) for y in possibAns))
