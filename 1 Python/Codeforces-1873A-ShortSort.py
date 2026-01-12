n = int(input())
allowed = ["abc","acb","bac","cba"]

for _ in range(n):
    print("Yes" if str(input()) in allowed else "No")
