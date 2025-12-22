n = int(input())
asL = list(map(int, input().split()))
maxL = [1]
for i in range(n-1):
    if asL[i+1]-asL[i]>0:
        maxL[-1]+=1
    else:
        maxL += [1]

print (max(maxL))
    
