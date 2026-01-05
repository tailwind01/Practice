nc = int(input())

for _ in range(nc):
    words = list(map(str, input().rstrip().split()))
    f_f_l = words[0][0]
    s_f_l = words[1][0]
    
    newA, newB = s_f_l+words[0][1:], f_f_l+words[1][1:]
    
    print(newA,newB)
