#whilst the problem is pretty simple to visualize, due to nature of the inputs
#we have to be mindful of the time and memory constraints
#v3 - 390ms runtime, 26200Kb memory
tc = int(input())

for _ in range(tc):
    np = int(input())
    strengths = list(map(int, input().rstrip().split()))
    max1=0
    max2=0
    for s in strengths:
        if s>max1:
            max2 = max1 #we perform the demotion of max1 to max2
            max1=s #we perform the promotion of s to max1

        elif s>max2:
            max2=s
    
    ansArr = []
    
    for i in range(np):
        currStr = strengths[i]
        if currStr!=max1:
            ansArr.append(currStr-max1)
        else:
            ansArr.append(currStr-max2)
    
    print (*ansArr)


#v2 - 359ms runtime, 26000kb memory
tc = int(input())

for _ in range(tc):
    np = int(input())
    strengths = list(map(int, input().rstrip().split()))
    sortedS = sorted(strengths)
    ansArr = []
    for i in range(np):
        currStr = strengths[i]
        if currStr!=sortedS[-1]:
            ansArr.append(currStr-sortedS[-1])
        else:
            ansArr.append(currStr-sortedS[-2])
    
    print (*ansArr)

#v1.2 TLE Code - 2000ms time, 26200Kb -second f-up
tc = int(input())

for _ in range(tc):
    np = int(input())
    strengths = list(map(int, input().rstrip().split()))
    maxS = max(strengths)
    ansArr = []
    for i in range(np):
        currStr = strengths[i]
        if currStr!=maxS:
            ansArr.append(currStr-maxS)
        else:
            if i==0:
                maxN = max(strengths[1:])
                ansArr.append(currStr-maxN)
            
            elif i!=0 and i!=(np-1):
                lmax = max(strengths[:i])
                rmax = max(strengths[i+1:])
                maxN = max(lmax,rmax)
                ansArr.append(currStr-maxN)
            
            else:
                maxN = max(strengths[:np-1])
                ansArr.append(currStr-maxN)
        
    
    print(*ansArr)

#v1.1 - 2000ms, first f-up
tc = int(input())

for _ in range(tc):
    np = int(input())
    strengths = list(map(int, input().rstrip().split()))
    sSet = sorted(set(strengths))
    maxStrength = max(strengths)
    ansArr = []
    for s in strengths:
        if s!=maxStrength:
            app = s-maxStrength
        else:
            if len(sSet)>1 and strengths.count(maxStrength)==1:
                app = s-sSet[-2]
            else:
                app = 0
    
        ansArr.append(app)
    
    print(*ansArr)


