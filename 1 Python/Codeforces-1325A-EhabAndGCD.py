# it is basically a simple mathematical observation
# since the solution is guaranteed
# instead of looping over pairs, we can just take 1 as first number
# so the second number would x-1, that's it

nc = int(input())

for _ in range(nc):
    x = int(input())
    ans = [x-1,1]
    print(*ans)
