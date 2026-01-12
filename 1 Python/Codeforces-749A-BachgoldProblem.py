def bachgoldMax(n):
    m = n%2
    intDiv = n//2
    result = []
    if m==1:
        result.append(str(intDiv))
        result.append("2 "*(intDiv-1))
        result.append("3")
    else:
        result.append(str(intDiv))
        result.append("2 "*(intDiv-1))
        result.append("2")
    
    print (result[0])
    return ("".join(result[1:]))

ni = int(input())

print(bachgoldMax(ni))
