nc = int(input())

for _ in range(nc):
    gs = int(input())
    grid = []
    for i in range(gs):
        lstr = str(input())
        grid.append(lstr)

    comparison = 1
    for j in range(1,len(grid)):
        prev = grid[j-1]
        curr = grid[j]
        boolS = 0
        if '1' in prev and '1' in curr:
            for c in range(len(curr)):
                boolS+=int(curr[c])-int(prev[c])
        comparison+=boolS

    print("SQUARE" if comparison==1 else "TRIANGLE")
