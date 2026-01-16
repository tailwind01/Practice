nc = int(input())

for _ in range(nc):
    inpStr= str(input())
    output = []
    
    for l in inpStr:
        if l=="p":
            output.append("q")
        elif l=="q":
            output.append("p")
        else:
            output.append("w")
    
    print("".join(output[::-1]))
