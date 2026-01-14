class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # as the problem is classfied under fibonacci series, we try with a cumulative approach
        cumulativecost = cost
        for x in range(2,len(cumulativecost)):
            cumulativecost[x]+=min(cumulativecost[x-1],cumulativecost[x-2])
        return min(cumulativecost[-1],cumulativecost[-2])
