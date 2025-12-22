#/tailwind publication
import string as s

initCols = list(s.ascii_uppercase)

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        
        ansStr = ""
        
        while columnNumber:
            columnNumber -= 1
            ansStr += initCols[columnNumber%26]
            columnNumber //= 26
        
        return ansStr[::-1]
