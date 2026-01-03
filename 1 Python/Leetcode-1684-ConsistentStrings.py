class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        resultcount = 0
        for word in words:
            boolcounter = 1
            for c in word:
                if c not in allowed:
                    boolcounter = 0
                    break
            if boolcounter == 1:
                resultcount+=1
    
        return resultcount
