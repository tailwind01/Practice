n,x = map(int, input().rstrip().split())
icecreams = x
distressed = 0

for i in range(n):
    inpL = list(map(str,input().rstrip().split()))
    if inpL[0]=="+":
        icecreams+=int(inpL[1])
    else:
        if int(inpL[1])<=icecreams:
            icecreams-=int(inpL[1])
        else:
            distressed+=1

ans = [icecreams, distressed]

print(*ans)
