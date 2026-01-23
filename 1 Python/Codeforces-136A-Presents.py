numFriends = int(input())
giftsOut = list(map(int,input().rstrip().split()))

rcpt = []

for i in range(numFriends):
    rcpt+=[str(giftsOut.index(i+1)+1)]

print(" ".join(rcpt))
