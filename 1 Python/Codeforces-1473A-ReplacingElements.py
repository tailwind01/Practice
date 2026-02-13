nc = int(input())

for _ in range(nc):
    n,d = map(int, input().rstrip().split())
    array = sorted(list(map(int, input().rstrip().split())))
    initSum = array[0]+array[1]
    ansBool = "Yes"
    for i in array:
        if min(i,initSum)>d:
            ansBool="No"
            break
    print(ansBool)
