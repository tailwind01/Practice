# 2 approaches, one using numpy, another using standard python lists

from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        row_maxes = [0] * N
        col_maxes = [0] * N
        for r in range(N):
            for c in range(N):
                val = grid[r][c]
                if val > row_maxes[r]:
                    row_maxes[r] = val
                if val > col_maxes[c]:
                    col_maxes[c] = val
        ans = 0
        for r in range(N):
            r_max = row_maxes[r]
            for c in range(N):
                ans += min(r_max, col_maxes[c]) - grid[r][c]
        return ans

import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        dims = len(grid)
        npGrid = np.array(grid)
        colMax = np.max(npGrid,axis=0)
        rowMax = np.max(npGrid,axis=1).reshape(-1,1)
        lims = np.minimum(colMax,rowMax)
        return int(np.sum(lims-npGrid))

import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        dims = len(grid)
        npGrid = np.array(grid)
        colMax = np.max(npGrid,axis=0)
        rowMax = np.max(npGrid,axis=1)
        ans = 0
        for i in range(dims):
            for j in range(dims):
                ans += min(rowMax[i],colMax[j])-grid[i][j]
        return int(ans)
