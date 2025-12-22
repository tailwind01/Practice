#/tailwind code, 77ms runtime
num = int(input())
initlist = [[1]*num]

for i in range(1,num):
    subl = []
    for j in range(num):
        if j==0:
            subl+=[1]
        else:
            calc = initlist[-1][j]+subl[-1]
            subl+=[calc]
    initlist+=[subl]

print(initlist[-1][-1])
