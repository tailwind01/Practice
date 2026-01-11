class Solution:
    def sum_of_squares(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit * digit
        return total_sum

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = self.sum_of_squares(n)
        return n == 1
