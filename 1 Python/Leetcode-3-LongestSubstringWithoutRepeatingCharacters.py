class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            max_length = max(max_length, right - left + 1)
            char_map[char] = right
        return max_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        ans = 0
        for i in range(l):
            subs = s[i]
            ssl=1
            for j in range(i+1,l):
                letter = s[j]
                if letter not in subs:
                    subs+=letter
                    ssl+=1
                else:
                    break
            if ssl>ans:
                ans = ssl
        return ans
