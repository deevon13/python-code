# Write a program to find the roots of a quadratic equation
# The equation is of the form ax^2 + bx + c = 0

from math import *
print("enter the values of a, b, and c of quardatic equation:")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=pow(b,2)-4*a*c
if d==0:
    print("the roots are real and equal")
    r1=r2=-(b/2*a)
    print(f"the roots are:{r1}and{r2}")
elif d>0:
    print("the roots are real and distinct")
    r1=(-b+sqrt(d))/(2*a)
    r2=(-b-sqrt(d))/(2*a)
    print(f"the roots are:{r1}and{r2}")
elif d<0:
    d=-d
    print("the roots are imaginary")
    real=-(b/2*a)
    img=sqrt(d/(2*a))  
    r1=complex(real, img)
    r2=complex(real, -img)
    print(f"the roots are;{r1}and{r2}")






