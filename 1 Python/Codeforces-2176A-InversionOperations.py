nc = int(input())

for _ in range(nc):
    operations = 0
    n = int(input())
    currlist = list(map(int, input().rstrip().split()))
    garbageCollection = []
    for x in range(1,n):
        if currlist[x]<currlist[x-1]:
            garbageCollection.append(x)
            currlist[x]=currlist[x-1] #this replacement helps keep order of the list as required
            operations+=1
        else:
            continue

    print(operations)





