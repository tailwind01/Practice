##given a list of unsorted integers, find all the numbers with minimum difference in the array
#code by tailwind, efficient enough to pass the ultimate testcase.

def closestNumbers(arr):
    arr.sort()
    minDiff = 2*10**7
    ansArr = []
    for i in range(1,len(arr)):
        if arr[i]-arr[i-1] < minDiff:
            minDiff = arr[i]-arr[i-1]
            ansArr.clear()
            ansArr+= [str(arr[i-1]), str(arr[i])]
        elif arr[i]-arr[i-1] == minDiff:
            ansArr+= [str(arr[i-1]), str(arr[i])]
    
    return " ".join(ansArr)

s = int(input())
inpL = list(map(int, input().rstrip().split()))
print(closestNumbers(inpL))
