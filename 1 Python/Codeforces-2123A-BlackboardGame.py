def solve(x):
    return "Bob" if x%4==0 else "Alice"

nc = int(input())

for _ in range(nc):
    n = int(input())
    print(solve(n))
