#v2 of the code - the pure mathematical reasoning
nc = int(input())

for _ in range(nc):
    size = int(input())
    array = list(map(int, input().rstrip().split()))
    set_arr = set(array)
    
    if len(set_arr)==1: #this is a trivial case, whereby indices 0 and 1 would be problematic
        print("NO")
    else:
        #the greediest approach would be initiate with the largest possible element and keep rest as-is
        ans = [array[-1]]+array[:-1]
        print("YES")
        print(*ans)


#v1 of the code - to gauge the intuition of solving the problem

nc = int(input())

for _ in range(nc):
    size = int(input())
    array = list(map(int, input().rstrip().split()))
    set_arr = set(array)
    
    if len(set_arr)==1:
        print("NO")
    else:
        ansArr = [array[-1],array[0]] # we start off with the maxima minima pairing
        for x in range(1, size-1):
            if x%2!=0:
                ansArr.append(array[x])
            else:
                if size%2==0: ansArr.append(array[size-x])
                else: ansArr.append(array[size-x-1])
        print("YES")
        print(*ansArr)
