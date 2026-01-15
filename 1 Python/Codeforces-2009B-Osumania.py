nc = int(input())

for _ in range(nc):
    size = int(input())
    ansL_raw = []
    for n in range(size):
        step = str(input())
        ansL_raw.append(step.index("#")+1)
    
    finAns = ansL_raw[::-1]
    print(" ".join(str(i) for i in finAns))
