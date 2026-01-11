nc = int(input())

for _ in range(nc):
    n = int(input())
    a = str(input())
    beganTask = [a[0]]
    
    for l in a:
        if beganTask[-1]!=l:
            beganTask.append(l)
    
    flag = 0
    for t in range(len(beganTask)):
        if beganTask[t] in beganTask[:t]:
            flag = 1
    
    
    print("No" if flag==1 else "Yes")
