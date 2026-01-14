nc = int(input())

for _ in range(nc):
    inpStr = str(input())
    
    if inpStr[-1]=="s":
        print(inpStr[:-2]+"i")
    else:
        print(inpStr[:-1]+"us")
