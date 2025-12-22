#/ simple implementation by tailwind, commonsensical!
import string as s
low = s.ascii_lowercase #listing all the lowercase letters
def theLoveLetterMystery(s):
    moves = 0
    for i in range(len(s)):
        if s[i]==s[len(s)-i-1]:
            continue
        else:
            moves+=abs(low.index(s[i])-low.index(s[len(s)-i-1]))
    return moves//2
numcases = int(input())
for _ in range(numcases):
    gs= input()
    print(theLoveLetterMystery(gs))
