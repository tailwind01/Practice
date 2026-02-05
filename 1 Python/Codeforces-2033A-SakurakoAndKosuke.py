def solve(x):
    return "Sakurako" if x%2==0 else "Kosuke"

nc = int(input())

for _ in range(nc):
    n = int(input())
    print(solve(n))
