class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        n = len(digits)
        for i in range(n-1,-1,-1):
            ans+=pow(10,n-i-1)*digits[i]
        ans+=1
        ansStr = str(ans)
        finAns = [int(s) for s in ansStr]
        return finAns
