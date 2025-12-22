#Codeforces 1343B - constructing a balanced array
#publisher tailwind, runtime 171ms, memory 16100 kb at ultimate test case level
#have to construct a mixed array of even and odd integers ensuring the sum of two halves (even half and odd half) is equal
#code below
def arCons(n):
    firstDiv = n//2
    if firstDiv % 2!=0: #case by hypothesis where array construction with last number being odd is not possible, modulo taken twice w.r.t 2
        return "NO"
    else: #array construction
        mp = firstDiv
        evenNums = []
        oddNums = []
        #constructing even nums
        for i in range(1,mp+1):
            num = i*2
            evenNums += [num]
        #constructing odd nums except last one
        for i in range(mp-1):
            odnum = i*2 + 1
            oddNums+= [odnum]
        lastOdd = sum(evenNums)-sum(oddNums)
        oddNums.append(lastOdd)
        finalAr = evenNums+oddNums
        ansAr = []
        for j in finalAr:
            ansAr+=[str(j)]
        return "YES"+"\n"+" ".join(ansAr)

nc = int(input())
for _ in range(nc):
    num = int(input())
    print(arCons(num))
