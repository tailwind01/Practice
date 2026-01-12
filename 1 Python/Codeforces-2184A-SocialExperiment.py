def socialExp(n):
    if n<=3:
        return n
    else:
        return n%2

nc = int(input())

for _ in range(nc):
    num = int(input())
    print(socialExp(num))

