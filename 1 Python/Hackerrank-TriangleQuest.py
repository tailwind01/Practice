#the problem asked to create a triangle specified in the range
#1,22,333,4444,55555 etc. without using string methods
#used geometric progression formula and took out only the int part

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (int(i*(pow(10,i))/(10-1))) #using geometric progression and basic algebra
