# Multiple versions of the solution sorted in an ascending order of runtime
class Solution:
    def minPartitions(self, n: str) -> int:
        for i in "987654321":
            if i in n: return int(i)

class Solution:
    def minPartitions(self, n: str) -> int:
        sieve = "987654321"
        for i in sieve:
            if i in n:
                return int(i)
                break

class Solution:
    def minPartitions(self, n: str) -> int:
        sieve = ["9","8","7","6","5","4","3","2","1"]

        for i in sieve:
            if i in n:
                return int(i)
                break

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(sorted(n)[-1])

class Solution:
    def minPartitions(self, n: str) -> int:
        maxInt = 0
        for i in n:
            if (int(i))>maxInt:
                maxInt = int(i)
        return maxInt
