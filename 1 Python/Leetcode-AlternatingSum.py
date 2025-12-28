class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        newArr = []
        for i in range(len(nums)):
            if i%2==0:
                newArr.append(nums[i])
            else:
                newArr.append(-1*nums[i])
        return sum(newArr)
        