class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        init_l,init_w = area,1
        upperL = int(area**(0.5)//1 + 1) #square root of the area (so that l > w)
        possibPairs = [[init_l,init_w]]
        for x in range(1, upperL):
            if area%x == 0:
                possibPairs.append([x,int(area//x)])
        return possibPairs[-1][::-1]
