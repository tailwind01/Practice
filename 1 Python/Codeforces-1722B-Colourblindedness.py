def cbRep(s1, s2):
    blindTo = ["B","G"]
    s1RepL = [str(1) if s1[x] not in blindTo else str(0) for x in range(len(s1))]
    s2RepL = [str(1) if s2[x] not in blindTo else str(0) for x in range(len(s2))]
    
    s1RepS = "".join(s1RepL)
    s2RepS = "".join(s2RepL)
    
    return s1RepS==s2RepS


nc = int(input())

for _ in range(nc):
    cols = int(input())
    str1 = str(input())
    str2 = str(input())
    
    print("Yes" if cbRep(str1,str2) else "No")
