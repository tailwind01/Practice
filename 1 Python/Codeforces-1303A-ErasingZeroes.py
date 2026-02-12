#v2
nc = int(input())

for _ in range(nc):
    ci = str(input())
    if '1' in ci:
        indf1 = ci.index('1')
        indl1 = len(ci)-ci[::-1].index('1')
        opers = ci[indf1:indl1].count('0')
        print(opers)
    else:
        print('0')

#v1
nc = int(input())

for _ in range(nc):
    ci = str(input())
    indColl = [i for i,c in enumerate(ci) if c=='1']
    opers = 0
    for j in range(1,len(indColl)):
        opers+=indColl[j]-indColl[j-1]-1
    print(opers)
