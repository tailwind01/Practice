class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        acrossX = sorted(points, key = lambda x: x[0])
        maxArea = 0
        for p in range(1,len(acrossX)):
            curr = acrossX[p][0]-acrossX[p-1][0]
            if curr>maxArea:
                maxArea = curr
        return maxArea
