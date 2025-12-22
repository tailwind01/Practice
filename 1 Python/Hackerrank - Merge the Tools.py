#/simple function definition
def merge_the_tools(string, k):
    subrange = len(string)//k
    ansStr = []
    for i in range(subrange):
        substr = ''
        for j in range(i*k,(i+1)*k):
            relLet = string[j]
            if relLet not in substr:
                substr+=relLet
        ansStr+=[substr]
    print("\n".join(ansStr))
