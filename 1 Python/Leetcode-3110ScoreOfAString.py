class Solution:
    def scoreOfString(self, s: str) -> int:
        AbsDiffSum = 0
        for c in range(len(s)-1):
            absDiff = abs(ord(s[c])-ord(s[c+1]))
            AbsDiffSum+=absDiff

        return AbsDiffSum
