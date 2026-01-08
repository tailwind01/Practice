nc = int(input())

for _ in range(nc):
    inpStr = str(input())
    
    if inpStr.count("A")>inpStr.count("B"):
        print("A")
    else:
        print("B")
