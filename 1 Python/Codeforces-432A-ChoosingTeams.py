n,k = map(int, input().rstrip().split())
pArr = list(map(int, input().rstrip().split()))

possibleParticipants = [] 

for p in pArr:
    if (5-p)>= k :
        possibleParticipants.append(p)
        
print(len(possibleParticipants)//3)
