#/tailwind implementation
import math as m
x=int(input())
y=int(input())
degreeSym = chr(176)

print(str(round(m.degrees(m.atan2(x,y))))+degreeSym)
