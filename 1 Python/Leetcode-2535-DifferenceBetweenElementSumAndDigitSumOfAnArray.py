class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum = sum(nums)
        strNums = ""
        for n in nums:
            strNums+=str(n)
        dsum = 0
        for d in strNums:
            dsum+=int(d)
        return esum-dsum
