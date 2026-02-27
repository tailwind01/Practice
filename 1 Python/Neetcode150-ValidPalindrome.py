class Solution:
    def isPalindrome(self, s: str) -> bool:
        collection = ""
        allowed = "abcdefghijklmnopqrstuvwxyz0123456789"
        for c in s:
            if c.lower() in allowed:
                collection+=c.lower()
        return collection==collection[::-1]
