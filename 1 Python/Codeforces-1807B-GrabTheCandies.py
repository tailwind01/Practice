nc = int(input())

for _ in range(nc):
    size = int(input())
    nums = list(map(int, input().rstrip().split()))
    evenSum = 0
    oddSum = 0
    for n in nums:
        if n%2==0:
            evenSum+=n
        else:
            oddSum+=n

    print("Yes" if evenSum>oddSum else "No") #the strict condition is Mihai greater than Bianca
