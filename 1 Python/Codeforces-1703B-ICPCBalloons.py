# define the balloon counter function first
def bc(s):
    count = 0
    for c in range(len(s)):
        # first occurrence of a letter gets 2 balloons
        if s[c] not in s[:c]:
            count+=2
        else:
            count+=1
    
    return count

nc = int(input())

for _ in range(nc):
    l = int(input())
    currStr = str(input())
    print(bc(currStr))
