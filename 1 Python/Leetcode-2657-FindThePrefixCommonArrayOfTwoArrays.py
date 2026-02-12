class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = []
        seenB = []
        ansArr = []
        commonCt = 0
        for i in range(len(A)):
            ai = A[i]
            bi = B[i]
            seenA.append(ai)
            seenB.append(bi)
            if bi in seenA:
                commonCt+=1
            if ai in seenB:
                commonCt+=1
            if ai==bi:
                commonCt-=1 #to correct for doublecount
            ansArr.append(commonCt)
        return ansArr
