# using collections counter

from collections import Counter as ctr
nc = int(input())

for _ in range(nc):
    n,m = map(int,input().rstrip().split())
    probs = str(input())
    oneRd = "ABCDEFG"
    reqRds = oneRd * m
    qBankNums = ctr(probs)
    reqRdsCounter = ctr(reqRds)
    newQs = reqRdsCounter-qBankNums
    
    print(sum(newQs.values()))
