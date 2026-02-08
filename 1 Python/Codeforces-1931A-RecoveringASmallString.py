import string as s

nc = int(input())

for _ in range(nc):
    tgt = int(input())
    letters = s.ascii_lowercase
    last = letters[min(26,tgt-2)-1] # as there are 2 letters before this letter
    tgt -= min(26,tgt-2)
    middle = letters[min(26,tgt-1)-1] # as there is 1 letter before this letter
    tgt -= min(26,tgt-1)
    first = letters[min(26,tgt)-1]
    opstr = [first, middle, last]
    print("".join(opstr))
