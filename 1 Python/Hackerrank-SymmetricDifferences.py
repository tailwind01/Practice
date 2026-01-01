m = int(input())
a = list(map(int, input().rstrip().split()))
n = int(input())
b = list(map(int, input().rstrip().split()))
valueDict= set(a+b)
duplicateNums = [x for x in valueDict if x in a and x in b ]
uniqueNums = [y for y in valueDict if y not in duplicateNums]

for z in sorted(uniqueNums):
    print(z)
