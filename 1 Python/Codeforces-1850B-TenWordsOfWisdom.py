# v2 of the code, processing at input stage only
nc = int(input())

for _ in range(nc):
    size = int(input())
    maxBi = 0
    for i in range(size): # we try to filter the answer at taking input itself without storing much in memory
        ai,bi = map(int,input().rstrip().split())
        if ai<=10 and bi>maxBi:
            maxBi = bi
            ans = i+1 #using this if condition we have ensured that the max quality always wins
    
    print(ans)
####=========================================================================================########

#v1 : first principles approach (needs two traversals over the list)
nc = int(input())

for _ in range(nc):
    size = int(input())
    respArr = []
    
    for i in range(size):
        ai,bi = map(int,input().rstrip().split())
        respArr.append((ai,bi))
    
    maxQual = 0
    ans = 0
    for t in range(len(respArr)):
        currTuple = respArr[t]
        if currTuple[0]<=10 and currTuple[1]>maxQual: #the conditions to be followed
            maxQual = currTuple[1]
            ans = t+1
    
    print(ans)


