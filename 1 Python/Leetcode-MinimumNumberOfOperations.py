# 2 versions
# v2 - left to right and right to left lookup

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        ansArr = [0] * size

        # left to right
        lCt = 0
        opL = 0
        for i in range(size):
            ansArr[i]+=opL
            if boxes[i]=='1':
                lCt+=1
            opL+=lCt
        
        #right to left
        rCt = 0
        opR = 0
        for j in range(size-1,-1,-1):
            ansArr[j]+=opR
            if boxes[j]=='1':
                rCt+=1
            opR+=rCt
        
        return ansArr


#v1 O(N^2) BruteForce first principles approach

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #actually since in one move only one ball can be moved, this can be approached step by step
        indsOf1 = []

        for i in range(len(boxes)):
            if boxes[i]=="1":
                indsOf1.append(i+1)
        
        ansArr = []
        
        for j in range(len(boxes)):
            moves = 0
            for k in indsOf1:
                moves+=abs(k-(j+1))
            ansArr.append(moves)
        
        return ansArr

