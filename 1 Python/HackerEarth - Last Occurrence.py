#/ a tailwind code
size, elem = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
flag = 0 
ans = 0
for j in range(size-1,0,-1):
    if arr[j]==elem:
        ans = j+1
        flag= 1
        break

if flag==1:
    print(ans)
else:
    print(-1)
