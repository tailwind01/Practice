# 2 versions
# v2
tc = int(input())

for _ in range(tc):
    n,k,x = map(int, input().rstrip().split())
    ansArr = []
    if x != 1:
        ansArr = [1] * n
        print("YES")
        print(n)
        print(*ansArr)
    elif k == 1 or (k == 2 and n % 2 != 0):
        print("NO")
    else:
        if n % 2 == 0:
            count = n // 2
            ansArr = [2] * count
        else:
            count = ((n - 3) // 2) + 1
            ansArr = [2] * (count - 1) + [3]
        print("YES")
        print (count)
        print(*ansArr)

#v1
tc = int(input())

for _ in range(tc):
    n,k,x = map(int, input().rstrip().split())
    allowed = [i if i!=x else 0 for i in range(1,k+1)]
    allowed.remove(0)
    allowed = allowed[::-1]
    ansArr = []
    
    if allowed:
        while(sum(ansArr)<n):
            needed = n-sum(ansArr)
            if needed in allowed:
                ansArr.append(needed)
            else:
                ansArr.append(allowed[-1])
        else:
            if sum(ansArr)==n:
                print("YES")
                print(len(ansArr))
                print(*ansArr)
            else:
                print("NO")
    else:
        print("NO")
