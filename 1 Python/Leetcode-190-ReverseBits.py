class Solution:
    def reverseBits(self, n: int) -> int:
        BinRep = str(format(n,'032b'))
        result = 0
        for i in range(len(BinRep)):
            result+= int(BinRep[i])*((2**(i)))
        return result
