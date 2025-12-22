#/ tailwind code, works well for large testcases as well  
daystr = []
for d in range(1,31):
    daystr+=[str(d)]

ms = int(input())
disc = []

for _ in range(ms):
    messg = list(map(str, input().rstrip().split()))
    if messg[0]=='G:':
        for m in messg:
            if m in daystr:
                disc+=[[2,m]]
    else:
        for m in messg:
            if m in daystr:
                disc+=[[1,m]]
    
forDate = 0
againstDate = 0

for d in disc:
    if d[1] in ["19","20"]:
        forDate+=int(d[0])
    else:
        againstDate+=int(d[0])

if forDate>againstDate:
    print("Date")
else:
    print("No Date")

    
