nc = int(input())

for _ in range(nc):
    latin_solve = ["A","B","C"]
    answer = ""
    for i in range(3): # we try to filter the answer at taking input itself without storing much in memory
        currBuffer = str(input())
        if "?" in currBuffer:
            for l in latin_solve:
                if l not in currBuffer:
                    answer = l
                    break #we get the eff out after finding the answer :D
    print(answer)
