#Write a program to find simple interest. Read principle, time and rate from the user.

print("enter principal,time and rate:")
p=int(input("principal:"))
r=int(input("rate:"))
t=int(input("time:"))
si=(p*t*r)/100
print("the simple interest is ",si)
