tc = int(input())

for _ in range(tc):
    n,m = map(int,input().rstrip().split())
    colwise = [""]*m #input collection in a columnwise manner
    for r in range(n):
        cs = str(input())
        for c in range(m):
            colwise[c]+=cs[c]

    target = ['v', 'i', 'k', 'a']
    found_idx = 0
    for s in colwise:
        if found_idx < len(target) and target[found_idx] in s:
            found_idx += 1

    print("Yes" if found_idx == len(target) else "No")
