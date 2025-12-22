#/ commonsense tailwind
from collections import Counter as ctr
nsh = int(input())
sizeAr = list(map(int, input().rstrip().split()))
unSizes = list(ctr(sizeAr).keys())
sizeAvail = list(ctr(sizeAr).values())
rev = 0
ncustom = int(input())

for _ in range(ncustom):
    sr, price = map(int, input().rstrip().split())
    if sr in unSizes:
        relInd = unSizes.index(sr)
        if sizeAvail[relInd]>=1: #sale made only if size is available and quantity is available. Once sale is made, quantity goes down by 1
            rev+=price
            sizeAvail[relInd]-=1

print(rev)
