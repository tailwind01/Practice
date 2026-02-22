# 2 versions of the solution, which are similar to each other..
#
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums),2):
            nums[i+1],nums[i] = nums[i],nums[i+1]
        return nums


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nS = sorted(nums)
        for i in range(1,len(nums),2):
            a,b = nS[i-1],nS[i]
            arr.append(b)
            arr.append(a)
        return arr
