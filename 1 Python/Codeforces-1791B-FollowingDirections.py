nc = int(input())

for _ in range(nc):
    size = int(input())
    steps = str(input())
    horizontal = ["R","L"]
    vertical = ["U","D"]
    xLocn = [0]
    yLocn = [0]
    
    
    for step in steps:
        currX = xLocn[-1]
        currY = yLocn[-1]
        newX = currX
        newY = currY
        if step in horizontal:
            if step == "R":
                newX+=1
            else:
                newX-=1
        else:
            if step == "U":
                newY+=1
            else:
                newY-=1
        xLocn.append(newX)
        yLocn.append(newY)
    
    flag = 0
    
    for l in range(len(xLocn)):
        if xLocn[l]==1:
            if yLocn[l]==1:
                flag=1
                break
        
    print("Yes" if flag==1 else "No")
