class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        lsum = nums[0]
        rsum = sum(nums)-lsum
        output = 0
        for n in nums[1:]:
            lsum+=n
            rsum-=n
            if (lsum-rsum)%2==0:
                output+=1
        return output

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        lsum = 0
        rsum = sum(nums)
        output = 0
        for n in nums[1:]:
            if (lsum-rsum)%2==0:
                output+=1
            lsum+=n
            rsum-=n
        return output
