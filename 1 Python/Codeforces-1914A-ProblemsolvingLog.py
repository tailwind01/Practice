import string as s
from collections import Counter as ctr

nc = int(input())

for _ in range(nc):
    m = int(input())
    prog = str(input())
    inctr = ctr(prog)
    probs = s.ascii_uppercase
    solved = 0
    for item,count in inctr.items():
        if count>=probs.index(item)+1:
            solved+=1
    print(solved)
