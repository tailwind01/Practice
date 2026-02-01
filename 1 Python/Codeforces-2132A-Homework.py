#v2 using deque (double ended lists)
from collections import deque as dq

t = int(input())

for _ in range(t):
    n = int(input())
    a = str(input())
    m = int(input())
    b = str(input())
    c = str(input())
    ans_dq = dq(a) # for convenience, we shall combine this later.., used deque for double ended lists
    for op in range(len(c)):
        if c[op] == "D":
            ans_dq.append(b[op])
        else:
            ans_dq.appendleft(b[op])
    print("".join(ans_dq))


# v1 normal approach without dq
t = int(input())

for _ in range(t):
    n = int(input())
    a = str(input())
    m = int(input())
    b = str(input())
    c = str(input())
    ansL = [char for char in a] # for convenience, we shall combine this later..
    for op in range(len(c)):
        if c[op] == "D":
            ansL.append(b[op])
        else:
            ansL.insert(0,b[op])
    print("".join(ansL))
