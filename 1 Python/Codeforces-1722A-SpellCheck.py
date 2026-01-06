# loading acceptable spelling characters in memory first
letters = ["T","i","m","u","r"]

nc = int(input())

for _ in range(nc):
    currNum = int(input())
    currBuffer = str(input())
    
    ctr = 1
    if currNum == 5: # we need to solve only if number of characters = 5
        for l in letters: #the loop should be on letters and not on currBuffer
            if l not in currBuffer:
                ctr = 0
                break
    else:
        ctr = 0
    print("Yes" if ctr==1 else "No")
