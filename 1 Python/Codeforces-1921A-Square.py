nc = int(input())

for _ in range(nc):
    #because we will have 4 points
    xCoords = []
    for i in range(4):
        xi,yi = map(int, input().rstrip().split())
        if xi not in xCoords:
            xCoords.append(xi)
        #we wont compute for the yi since it is a perfect square so we dont need y coordinates
    
    sideVal = max(xCoords)-min(xCoords)
    print(sideVal**2) #standard formula for area of square
