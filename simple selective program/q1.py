#Write a program to convert Cartesian coordinates to Polar coordinates

from math import *
print("enter cartesian coordinates:")
a=int(input("A:"))
b=int(input("B:"))
r=pow(a,2)+pow(b,2)
deg=degrees(atan2(a,b))
x=r*cos(deg)
y=r*sin(deg)
print(f"in polar form the coordinates are :{x}and{y}")

