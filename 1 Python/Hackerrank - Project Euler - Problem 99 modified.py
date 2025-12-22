import math as m
l = int(input())
mod = pow(10,9)+7

inpl=[]
for i in range(l):
    base, exponent = map(int, input().split())
    #we will calculate values using logarithmic rules
    ln_ans = exponent*m.log(base)
    inpl+=[[ln_ans, base, exponent]]

myl = sorted(inpl, key = lambda x:x[0])
k = int(input())

ans = []

for j in myl[k-1][1:]:
    ans+=[str(j)]

print(" ".join(ans))
