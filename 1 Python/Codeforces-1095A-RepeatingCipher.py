cs = int(input())
encoded = str(input())
ans = ""
ptr = 0
step = 1
while ptr<cs:
    ans+=encoded[ptr]
    ptr+=step
    step+=1
print(ans)
