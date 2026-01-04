class Solution:
    def countDigits(self, num: int) -> int:
        strNum = str(num)
        result = 0
        for s in strNum:
            int_s=int(s)
            if num%int(s)==0:
                result+=1
        return result
