nc = int(input())

for _ in range(nc):
    n = int(input())
    hashPiece = "##"
    dotPiece = ".."
    # we will ignore columns right now, as they will stack up automatically once we have rows figured out
    firstRow = ""
    thirdRow = "" #this will be dependent upon the the first row
    
    for a in range(0,2*n,2):
        aAsMultiple = a//2
        if aAsMultiple%2==0:
            firstRow+=hashPiece
            thirdRow+=dotPiece
        else:
            firstRow+=dotPiece
            thirdRow+=hashPiece
    
    for b in range(2*n):
        bAsMultiple = b//2
        if bAsMultiple%2==0:
            print(firstRow)
        else:
            print(thirdRow)
