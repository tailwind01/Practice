#/ simple python code, by tailwind, runtime 62ms, memory 0
nc = int(input())
for _ in range(nc):
    s = str(input())
    ans = ''
    for i in range(len(s)):
        if i%2==0 or i==len(s)-1:
            ans+=s[i]
    print(ans)
