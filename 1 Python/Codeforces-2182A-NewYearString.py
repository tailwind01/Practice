nc = int(input())

for _ in range(nc):
    m = int(input())
    strInput = str(input())
    if "2026" in strInput or "2025" not in strInput:
        print(0)
    else:
        print(1)
