#code by tailwind
#problem 1352A - Codeforces - Sum of Round Numbers

nc = int(input())
for _ in range(nc):
    ns = str(input())
    revd = ns[::-1]
    numAr =[]
    for d in range(len(ns)):
        if revd[d]!='0':
            calc = int(revd[d])*(10**d)
            numAr+=[str(calc)]
    print(len(numAr))
    print(' '.join(numAr))