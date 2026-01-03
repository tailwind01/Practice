class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        occurrences = 0
        for s in stones:
            if s in jewels:
                occurrences+=1
        return occurrences
