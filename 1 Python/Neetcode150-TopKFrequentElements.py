from collections import Counter as ctr
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCt = sorted(list(ctr(nums).items()),key=lambda x: x[1], reverse=True)
        ans = []
        for i in numsCt:
            if len(ans)<k:
                ans.append(i[0])
        return ans
