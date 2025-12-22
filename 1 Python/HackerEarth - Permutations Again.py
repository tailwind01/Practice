#/tailwind code, memory heavy, runtime efficient
#/ all testcases solved in 2s.
maxnum = pow(10,5)+1
ansAr = [0,1,1]
for j in range(3,maxnum):
    if j%2==0:
        mplier = j//2
        ansAr+=[mplier*j - 1]
    else:
        mplier = j//2
        addition = j//2 - 1
        ansAr+=[mplier*j + addition]

nc = int(input())

for _ in range(nc):
    n = int(input())
    if n==1:
        print(1)
    else:
        print(ansAr[n])
