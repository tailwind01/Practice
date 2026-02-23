tc = int(input())

for _ in range(tc):
    nchars = int(input())
    inpstr = str(input())
    uniques = list()
    res = ""
    for char in inpstr.lower():
        if not res or char != res[-1]:
            res += char
    print("YES" if res == "meow" else "NO")
