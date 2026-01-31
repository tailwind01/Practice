# given the constraints we operate in 32bit representation to find flips
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s32b = format(start,'032b')[2:]
        g32b = format(goal,'032b')[2:]
        moves = 0
        for c in range(len(g32b)):
            if s32b[c]!=g32b[c]:
                moves+=1
        return moves
