# a tailwind code, 77ms runtime, 0KB memory
nc = int(input())
for _ in range(nc):
    mn = int(input())
    s1 = []
    for i in range(1,mn+1):
        s1+=[i]
    myArr = s1[::-1]
    #we just swap till the midpoint and then continue with original array, so that the indices are unmatched
    midPoint = mn//2 
    ansAr = []
    for j in myArr[:midPoint]:
        ansAr+=[str(j)]
    for m in s1:
        if str(m) not in ansAr:
            ansAr+=[str(m)]
    if mn==2:
        print("2 1")
    else:
        print(" ".join(ansAr))
        
