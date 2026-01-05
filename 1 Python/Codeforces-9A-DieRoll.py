y,w = map(int, input().rstrip().split())
countFrom = max(y,w)

if countFrom==3 or countFrom == 5:
    ansNumerator = (6-countFrom+1)//2
    ansDenominator = 3
elif countFrom== 2 or countFrom == 6:
    ansNumerator = 6-countFrom+1
    ansDenominator = 6
elif countFrom == 1:
    ansNumerator = 1
    ansDenominator = 1
elif countFrom == 4:
    ansNumerator = 1
    ansDenominator = 2

print(str(ansNumerator)+"/"+str(ansDenominator))
