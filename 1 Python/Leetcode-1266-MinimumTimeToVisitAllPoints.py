class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            pt = points[i]
            npt = points[i+1]
            xdiff = abs(npt[0]-pt[0])
            ydiff = abs(npt[1]-pt[1])
            time+=max(xdiff,ydiff)
        return time
