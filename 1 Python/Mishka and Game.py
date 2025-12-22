t = int(input())
Mishka_ct = 0
Chris_ct=0
for i in range(t):
    case=list(map(int, input().split()))
    if case[0]>case[1]:
        Mishka_ct+=1
    elif case[0]<case[1]:
        Chris_ct+=1
    else:
        pass;
if Mishka_ct>Chris_ct:
    print("Mishka")
elif Chris_ct>Mishka_ct:
    print("Chris")
else:
    print("Friendship is magic!^^")
    
