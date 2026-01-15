import math as m

def isPerfectSquare(n):
    return m.sqrt(n)==int(m.sqrt(n))

nc=int(input())

for _ in range(nc):
    n = int(input())
    stArr = list(map(int, input().rstrip().split()))
    sieveSum = sum(stArr)
    print("Yes" if isPerfectSquare(sieveSum) else "No")
