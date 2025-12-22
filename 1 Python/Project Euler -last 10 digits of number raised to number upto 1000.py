#/ a tailwind pub
num = 0
for i in range(1,1001):
    num+=pow(i,i)

numasstr = str(num)
print(numasstr[-10:])
