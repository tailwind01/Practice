def colorOrBw(s1):
    uniqueToColor = ["C","M","Y"]
    for c in uniqueToColor:
        if c in s1:
            return True
    
    return False

r,c = map(int, input().rstrip().split())
grid = ""
for _ in range(r):
    currStrL = list(map(str,input().rstrip().split()))
    currStr = "".join(currStrL)
    grid+=currStr

print("#Color" if colorOrBw(grid) else "#Black&White")
