import string as s

nc = int(input())

for _ in range(nc):
    size = int(input())
    word = str(input())
    alphabet = s.ascii_lowercase
    print(alphabet.index("".join(sorted(word))[-1])+1)
