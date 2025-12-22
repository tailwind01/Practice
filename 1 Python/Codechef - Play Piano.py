#/tailwind pub
nc = int(input())

for i in range(nc):
    pl = str(input())
    days = len(pl)//2
    flag = 0
    for s in range(days):
        substr = pl[2*s:2*s+2]
        if substr in ['AB','BA']:
            continue
        else:
            flag=1
            break
    if flag==0:
        print('yes')
    else:
        print('no')
