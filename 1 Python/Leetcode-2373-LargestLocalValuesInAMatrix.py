import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        npg = np.array(grid)
        return np.max(swv(npg,(3,3)), axis = (2,3)).tolist()
