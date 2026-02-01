s = str(input())
t = str(input())

position = 1 #starts at position 1..

#we update position only if we have an operation that takes us ahead
for o in range(len(t)):
    if t[o]==s[position-1]:
        position+=1

print(position)
