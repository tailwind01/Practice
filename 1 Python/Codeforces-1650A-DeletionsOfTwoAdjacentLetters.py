nc = int(input())

for _ in range(nc):
    gs = str(input())
    s = str(input())
    ansBool = 0
    # hypothesis is that for a solution to exist, s must sit at an odd number in the string
    for c in range(len(gs)):
        if (c+1)%2!=0 and gs[c]==s:
            ansBool = 1
            break
    print("Yes" if ansBool==1 else "No")
