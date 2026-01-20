# Codeforces 1866A - Ambitious Kid
size = int(input())
inpArr = list(map(int,input().rstrip().split()))
absVals = [abs(x) for x in inpArr]
print(min(absVals))
