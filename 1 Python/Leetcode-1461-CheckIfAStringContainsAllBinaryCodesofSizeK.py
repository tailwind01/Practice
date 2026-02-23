# I tried a bruteforce approach that was logically sound, but encountered TLE
# Thereafter, I learned about the bitwise left shift operator approach to troubleshoot

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        reqd = 1 << k
        checked = set()
        for i in range(len(s) - k + 1):
            checked.add(s[i:i+k])
        return len(checked)==reqd

# Code that passed 199/201 test cases before encountering TLE
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ansBool = 1
        for i in range(pow(2,k)):
            binrep = format(i,'032b')[-k:]
            if binrep not in s:
                ansBool = 0
                break
        return ansBool==1
