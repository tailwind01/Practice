nc = int(input())

for _ in range(nc):
    pn = int(input())
    numstr = str(pow(2,pn))
    sumd = 0
    for j in numstr:
        sumd+=int(j)
    print(sumd)
