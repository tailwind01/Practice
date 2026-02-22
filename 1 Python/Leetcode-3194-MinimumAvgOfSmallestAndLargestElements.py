# 2 versions, both are efficient
#
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l = len(nums)
        msum = nums[0]+nums[-1]
        for i in range(1,l-1):
            s = nums[i]+nums[l-i-1]
            if s<msum:
                msum = s
        return msum/2

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l = len(nums) 
        return min([(nums[i]+nums[l-i-1])/2 for i in range(len(nums)//2)])

