#/ a tailwind code
def fibon_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
         fibs.append(fibs[-1] + fibs[-2])
    fibstr=[]
    for j in fibs:
        fibstr+=[str(j)]
    return fibstr

allStr = fibon_to(5000)      
for i in allStr:
    if len(i)==1000:
        print(allStr.index(i))
        break
