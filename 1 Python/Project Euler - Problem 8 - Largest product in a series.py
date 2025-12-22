#/ tailwind publication, easy, common-sense approach
l = 20
inpstr=''
for i in range(l):
    ss = str(input())
    inpstr+=ss

sl = len(inpstr)

maxprod = 1
for i in range(sl-13):
    stepprod = 1
    for j in range(i,i+13):
        num = inpstr[j]
        stepprod*=int(num)
    if stepprod>maxprod:
        maxprod=stepprod
print(maxprod)
