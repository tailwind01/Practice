nc = int(input())

for _ in range(nc):
    layout = str(input())
    toType = str(input())
    moves = 0
    letters = set(toType)
    if len(letters)>1:
        for x in range(1,len(toType)):
            moves+=abs(layout.index(toType[x])-layout.index(toType[x-1]))
    print(moves)
