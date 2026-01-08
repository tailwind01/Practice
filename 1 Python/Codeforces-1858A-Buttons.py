nc = int(input())

for _ in range(nc):
    buttons = list(map(int, input().rstrip().split()))
    anna = buttons[0]
    katie = buttons[1]
    either = buttons[2]
    
    total = sum(buttons)
    
    #only first two cases need computation, else the one with more nums of buttons to press will win 
    if anna==katie and total % 2 == 0:
        print("Second")
    elif anna==katie and total%2 ==1:
        print("First")
    else:
        if anna>katie:
            print("First")
        else:
            print("Second")
