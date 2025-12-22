#/ tailwind
maxnum = (pow(9,5))*5

nums = []

for i in range(2, maxnum+1):
    numstr = str(i)
    tmsum = 0
    for j in numstr:
        intj = int(j)
        tmsum+=pow(intj, 5)
    if tmsum==i:
        nums+=[i]
print(sum(nums))
