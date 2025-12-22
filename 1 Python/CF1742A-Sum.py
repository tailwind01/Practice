# thesis is that if the number is present which is a sum of the other two, we will have a total which is twice that particular number

t = int(input())
for _ in range(t):
     x,y,z = map(int, input().rstrip().split())
     tot = x+y+z
     one_half = tot/2
     if one_half in [x,y,z]:
         print ("YES")
     else:
         print("NO")



