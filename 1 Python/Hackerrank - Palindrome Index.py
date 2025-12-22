#a tailwind publication, try to be better everyday#
#you have to find index of the letter, sans which, the resulting string will be a palindrome.
#my code is very straight forward, and fortunately, it does not exceed time limit

def palindromeIndex(s):
    if s==s[::-1]:
        return -1
    else:
        for i in range(len(s)):
            if s[i]==s[len(s)-1-i]:
                continue
            else:
                ss1 = s[:i]+s[i+1:]
                ss2 = s[:len(s)-1-i]+s[len(s)-i:]
                if ss1==ss1[::-1]:
                    return i
                else:
                    return len(s)-1-i
                break
            
ncases = int(input())

for _ in range(ncases):
    inps = str(input())
    print(palindromeIndex(inps))
