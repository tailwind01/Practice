numArr = int(input())
origList = list(map(int, input().rstrip().split()))

serjaSum = 0
dimaSum = 0

for i in range(numArr):
    max_at_iter = 0
    if origList[0]>=origList[-1]:
        max_at_iter = origList[0]
        del origList[0]
    else:
        max_at_iter = origList[-1]
        del origList[-1]
    if i%2==0:
        serjaSum+=max_at_iter
    else:
        dimaSum+=max_at_iter

print(serjaSum,dimaSum)
    
