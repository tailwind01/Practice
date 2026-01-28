tc = int(input())

for _ in range(tc):
    str_n = str(input())
    flag = 0
    if len(str_n)>=3:
        firstTwo = str_n[:2]
        rest = str_n[2:]
        disallowed = ['0','1']
        
        if len(rest)==1:
            if (firstTwo == '10' and rest[0] not in disallowed):
                flag = 1
        else:
            if (firstTwo == '10' and rest[0]!='0'):
                flag = 1
    
    print("YES" if flag==1 else "NO")
