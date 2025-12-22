#Problem 427A - Police Recruits, CODEFORCES
#tailwind publication #runtime 109ms, memory 4900Kbs at the ultimate testcase level
#O(n) time
n = int(input())
sq = list(map(int, input().rstrip().split()))
ofCt = 0
unTr = 0
contCrCt = 0
for i in sq:
    if i > 0: #officer recruited
        ofCt += i
        continue
    if ofCt > 0 and i < 0: #crime occurred
        ofCt -= 1 #officer occupied
        continue
    if i < 0: #the untreated case residual
        unTr += 1

print(unTr)
