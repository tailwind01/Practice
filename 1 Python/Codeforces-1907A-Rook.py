nc = int(input())

for _ in range(nc):
    pos = str(input())
    horiz = pos[0]
    vert = int(pos[1])
    ansL = []
    for i in range(1,9,1):
        if i!= vert:
            sComb1 = horiz+str(i)
            ansL.append(sComb1)

    for j in 'abcdefgh':
        if j!=horiz:
            sComb2 = j+str(vert)
            ansL.append(sComb2)

    print("\n".join(ansL))
