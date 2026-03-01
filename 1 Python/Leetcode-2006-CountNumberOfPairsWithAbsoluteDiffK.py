# using dictionary mapping
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            below, above = num - k, num + k
            if below in seen:
                counter += seen[below]
            if above in seen:
                counter += seen[above]
            seen[num] += 1
        return counter


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pk = [n+k for n in nums]
        mk = [n-k for n in nums]
        ans = 0
        # we traverse from right..
        for i in range(len(nums)-1,0,-1):
            cn = nums[i]
            subl = pk[:i]+mk[:i]
            ans+=subl.count(cn)
        return ans


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)-1):
            cn = nums[i]
            rn1,rn2 = cn+k, cn-k
            if rn1 in nums[i+1:]:
                ans+=nums[i+1:].count(rn1)
            if rn2 in nums[i+1:]:
                ans+=nums[i+1:].count(rn2)

        return ans


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)-1):
            cn = nums[i]
            for j in range(i+1,len(nums)):
                iterNum = nums[j]
                if abs(iterNum-cn)==k:
                    ans+=1
        return ans
