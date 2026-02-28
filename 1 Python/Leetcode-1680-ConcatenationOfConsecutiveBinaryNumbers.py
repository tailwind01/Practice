class Solution:
    def concatenatedBinary(self, n: int) -> int:
        formed=""
        for i in range(1,n+1):
            formed+=bin(i)[2:]
        return int(formed,base=2)%(pow(10,9)+7)
