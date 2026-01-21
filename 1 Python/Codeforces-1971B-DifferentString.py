nc = int(input())

for _ in range(nc):
    s = str(input())
    s_s = set(s)
    
    if len(s_s)==1:
        print("NO")
    else:
        print("YES")
        print(s[-1]+s[0:-1])
