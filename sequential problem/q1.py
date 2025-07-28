#Write a program to calculate area and circumference of a circle. Read radius from user

from math import *
r=int(input("enter a radius:"))
area=pi*pow(r,2)
circ=2*pi*r
print(f"the area is {area} and {circ}")
