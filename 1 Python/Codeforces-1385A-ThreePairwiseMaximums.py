# 2 versions
# v2 - 156ms runtime

tc = int(input())

for _ in range(tc):
    sorted_xyz = sorted(list(map(int,input().rstrip().split())))
    
    if(sorted_xyz[1]!=sorted_xyz[2]):
        print("NO")
    else:
        print("YES")
        print(sorted_xyz[0],sorted_xyz[0],sorted_xyz[2])


# v1 - 250ms runtime
tc = int(input())

for _ in range(tc):
    sorted_xyz = sorted(list(map(int,input().rstrip().split())))
    set_xyz = set(sorted_xyz)
    
    if (len(set_xyz)==3) or (sorted_xyz[0]==sorted_xyz[1] and sorted_xyz[0]!=sorted_xyz[-1]):
        print("NO")
    elif len(set_xyz)==2 and sorted_xyz[-1]==sorted_xyz[-2]:
        ansArr = [sorted_xyz[0],sorted_xyz[0],sorted_xyz[1]]
        print("YES")
        print(*ansArr)
    else:
        print("YES")
        print(*sorted_xyz)
