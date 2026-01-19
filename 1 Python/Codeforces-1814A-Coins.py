def coins(a,b):
    # we need k only if a is not divisible by 2
    if a%2==0:
        return "Yes"
    else:
        if b % 2 != 0: 
            return "Yes"
        else:
            return "No"

nc = int(input())

for _ in range(nc):
    x,y = map(int, input().rstrip().split())
    print(coins(x,y))
