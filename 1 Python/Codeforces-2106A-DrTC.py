# concise code - after the logic met the conditions
nc = int(input())

for _ in range(nc):
    s = int(input())
    binary = str(input())
    ans = (s-1)*binary.count('1')+binary.count('0')
    print(ans)

# the logic delineating version of code
nc = int(input())

for _ in range(nc):
    s = int(input())
    binary = str(input())
    ans = s*binary.count('1')
    for i in range(s):
        if binary[i]=='1':
            ans-=1
        else:
            ans+=1
    print(ans)
