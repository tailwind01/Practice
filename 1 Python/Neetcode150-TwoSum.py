class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = [target-n for n in nums]
        ans = []
        for i in range(len(nums)-1,-1,-1):
            val = nums[i]
            if val in req:
                ans = [i,req.index(val)]
                break
        ans.sort()
        return ans
