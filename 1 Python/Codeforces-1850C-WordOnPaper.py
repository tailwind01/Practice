import string as s
nc=int(input())

for _ in range(nc):
    alphabet = s.ascii_lowercase
    word = "" #initialize an empty string
    
    for _ in range(8): #for 8 iterations
        currSieve = str(input())
        for l in currSieve:
            if l in alphabet:
                word+=l
    
    print(word)
