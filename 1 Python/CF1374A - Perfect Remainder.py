#Codeforces 1374A - Required remainder // a simple implementation
#a tailwind publication, runtime 524ms, memory 0Kb, at ultimate testcase level, big numbers with testcases being upto 50000 executed
#code
nc = int(input())
for _ in range(nc):
    x,y,n = map(int, input().rstrip().split())
    intDiv = n//x                             #seeing the integer division
    lastPerfDiv = intDiv*x                    #last perfect multiple of x
    ans = lastPerfDiv+y                       #the greatest number that would ensure a modulo==y
    if ans<=n:                                #to check whether it's in our range
        print(ans)
    else:                                     #if not in range, the last number in the range will be (answer-x), which also ensures a modulo == y
        print(ans-x)
