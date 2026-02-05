#v2 of the code
n = int(input())
istr = str(input())
ansBool = [1 if (istr[i]=="x" and istr[i-1]=="x" and istr[i-2]=="x") else 0 for i in range(2,n)]
print(sum(ansBool))

# v1 of the code
l = int(input())
istr = str(input())

ops = 0
x3coll = []

for i in range(l-2):
    if istr[i:i+3]=="xxx":
        x3coll.append(i+2) #we append removable x instance..

print(len(x3coll))
