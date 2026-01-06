a,b,c,d = map(int,input().rstrip().split())

inputStr = str(input())

calories = 0
for x in inputStr:
    #we put the characters in quotes as we have parsed them as components of a string
    #naming convention used x in the loop in this version of code to avoid confusion
    if x=="1":
        calories+=a
    elif x=="2":
        calories+=b
    elif x=="3":
        calories+=c
    elif x:
        calories+=d

print(calories)
