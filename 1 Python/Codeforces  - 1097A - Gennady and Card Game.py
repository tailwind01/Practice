#/tailwind code, 62ms runtime
tablecard = str(input())
cards = list(map(str, input().rstrip().split()))
hnum = 5
card = []
suits = []

for i in range(hnum):
    card+=cards[i][0]
    suits+=cards[i][1]

flag = 0

for j in range(hnum):
    if card[j] in tablecard or suits[j] in tablecard:
        flag=1
        break

if flag==1:
    print("YES")
else:
    print("NO")
    
