nc = int(input())
for _ in range(nc):
    a, b = map(int, input().rstrip().split())
    ct = 0
    for i in range(a,b+1):
        if str(i)==str(i)[::-1]:
            ct+=1
    print(ct)

```
### Testcase
#10
#31 62235
# 95 63494
# 21 86212
# 9 22300
# 36 7305
# 59 93613
# 53 3995
# 91 2195
# 93 54286
# 20 51609
###
```
