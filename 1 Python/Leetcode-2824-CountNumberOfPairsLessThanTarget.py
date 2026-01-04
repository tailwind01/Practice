class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        resultCount = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]<target:
                    resultCount+=1
        
        return resultCount
