# 2 versions of the code, v1 is a bruteforce triple loop
# v2 is a pointer approach kind of a solution
#
# v2
inpStr = input()
q_count = 0
qa_count = 0
total_qaq = 0
for char in inpStr:
    if char == "Q":
        total_qaq += qa_count
        q_count += 1   
    elif char == "A":
        qa_count += q_count

print(total_qaq)

#v1
inpStr = str(input())
opers = 0

for i in range(len(inpStr)-2):
    for j in range(i+1,len(inpStr)-1):
        for k in range(j+1,len(inpStr)):
            madeStr = inpStr[i]+inpStr[j]+inpStr[k]
            if madeStr=="QAQ":
                opers+=1

print(opers)
