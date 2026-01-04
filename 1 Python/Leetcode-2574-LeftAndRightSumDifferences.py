class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answerArray = []
        for i in range(len(nums)):
            if i==0:
                lsum = 0
                rsum = sum(nums[i+1:])
            elif i>0 and i<(len(nums)-1):
                lsum = sum(nums[:i])
                rsum = sum(nums[i+1:])
            else:
                lsum = sum(nums[:i])
                rsum =0
            answerArray.append(abs(lsum-rsum))
        return answerArray
