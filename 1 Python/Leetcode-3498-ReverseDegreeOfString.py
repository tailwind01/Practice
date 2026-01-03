class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        reversedAlphabet = alphabet[::-1]
        result = 0
        for i in range(len(s)):
            iterationVariable = (reversedAlphabet.index(s[i])+1)*(i+1)
            result+=iterationVariable
        return result
