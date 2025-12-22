#/simple code by tailwind
import string as s
initCols = list(s.ascii_uppercase)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        numfinderL = list(columnTitle)[::-1]
        
        colNum = 0
        if len(numfinderL)>1:
            for i in range(len(numfinderL)):
                relMultiple = i
                relInd = initCols.index(numfinderL[i])
                colNum+=(pow(26, relMultiple)*(relInd+1))
        else:
            colNum = initCols.index(columnTitle)+1
        
        return colNum
