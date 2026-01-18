nc = int(input())
for _ in range(nc):
    size = int(input())
    inp = list(map(int,input().rstrip().split())) 
    #since the list contains only 1 and 2, and 1 being trivial
    #the problem is identification of the midpoint of the counts of 2
    # lets approach it that way
    if 2 in inp:
        Ind2s = [i for i, val in enumerate(inp) if val==2]
        midPt = len(Ind2s)//2
        if len(Ind2s)%2==0:
            print(Ind2s[midPt-1]+1) #as python is 0-indexed
        else:
            print(-1)
    else: #for trivial case where there are no 2s
        print(1)
