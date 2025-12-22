#easy implementation by tailwind

n = int(input())
password = input()

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    nflag, lflag,uflag,sflag = 0,0,0,0
    for i in password:
        if i in numbers:
            nflag=1
        if i in lower_case:
            lflag=1
        if i in upper_case:
            uflag=1
        if i in special_characters:
            sflag=1
    ansL = [nflag, lflag, uflag, sflag]
    
    ans = ansL.count(0) 
    
    if (n+ans)<6:
        return 6-n
    else:
        return ans

print(minimumNumber(n,password))
