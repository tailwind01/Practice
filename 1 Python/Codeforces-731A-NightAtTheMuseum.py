import string as s
alphabet = s.ascii_lowercase
word = str(input())
rotations = [min(alphabet.index(word[0]), 26-alphabet.index(word[0]))] #listing the same so that we have an audit trail of distances traversed
cwDistArr = []
ccwDistArr = []
for l in range(1,len(word)):
    pLetter = word[l-1]
    cLetter = word[l]
    cwDist = abs(alphabet.index(cLetter)-alphabet.index(pLetter))
    ccwDist= 26-abs(alphabet.index(cLetter)-alphabet.index(pLetter))
    rotations.append(min(cwDist,ccwDist))

print(sum(rotations))
