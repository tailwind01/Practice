class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1,len(height)) if height[i-1]>threshold ]


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = [i for i in range(1,len(height)) if height[i-1]>threshold ]
        return ans


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i in range(1,len(height)):
            prev = height[i-1]
            if prev>threshold:
                ans.append(i)
        return ans
