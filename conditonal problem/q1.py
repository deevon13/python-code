#Find the area of a triangle when lengths of three sides are given. Check the validity of the triangle.

from math import *
a=int(input("enter first side of triangle:"))
b=int(input("enter second side of triangle:"))
c=int(input("enter third side of triangle:"))
s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
if(a+b>c) and (a+c>b) and (b+c>a):
    print("it is a valid triangle")
else:
    print("it is not a valid triangle")
print(f"area of triangle is {area}")
