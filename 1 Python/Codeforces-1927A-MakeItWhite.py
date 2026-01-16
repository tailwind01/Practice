nc = int(input())

for _ in range(nc):
    size = int(input())
    inpStr = str(input())
    inpStr_Rev = "".join(inpStr[::-1])
    
    print(size-inpStr.index("B")-inpStr_Rev.index("B"))
