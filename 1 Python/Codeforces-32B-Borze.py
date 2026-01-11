def BorzeDecoding(s):
    dmp = []
    allowed = [".","-.","--"]
    ti = []
    for c in range(len(s)):
        if s[c]=="." and c not in ti:
            dmp.append(s[c])
            ti.append(c)
        if s[c]=="-" and c not in ti:
            dmp.append(s[c:c+2])
            ti.append(c)
            ti.append(c+1)
    result = []
    for x in dmp:
        if x in allowed:
            result.append(str(allowed.index(x)))
    
    return "".join(result)
    

inputString = str(input())

print(BorzeDecoding(inputString))
