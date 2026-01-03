class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        vowFreqMax = 0
        consoFreqMax = 0
        for c in s:
            if c in vowels:
                if s.count(c)>vowFreqMax:
                    vowFreqMax = s.count(c)
            else:
                if s.count(c)>consoFreqMax:
                    consoFreqMax = s.count(c)

        return vowFreqMax+consoFreqMax
