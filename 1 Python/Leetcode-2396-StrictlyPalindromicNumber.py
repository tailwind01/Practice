def base_convert(x, b):
    result = ""
    while x > 0:
            result+=str(x % b)
            x = x // b
    return result[::-1]

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        sPalindromeCtr = 1
        for i in range(2,n-1):
            currRep = base_convert(n,i)
            if currRep == currRep[::-1]:
                continue
            else:
                sPalindromeCtr = 0
                break
        return bool(sPalindromeCtr)
