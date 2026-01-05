nc = int(input())

for _ in range(nc):
    
    currStr = str(input())
    comparison = "codeforces"
    takeout = 0
    for l in range(len(currStr)):
        if currStr[l]!=comparison[l]:
            takeout+=1
    print(takeout)
