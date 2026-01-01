en_n = int(input())
enRolls = list(map(int, input().rstrip().split()))
fr_n = int(input())
frRolls = list(map(int, input().rstrip().split()))
allRolls = set(enRolls+frRolls)
disJtCount = 0

for i in allRolls:
    if i not in frRolls or i not in enRolls:
        disJtCount+=1
        
print(disJtCount)
