#Write a program to find the total amount when compound interest is used for given years, rate and principle by the user.

print("enter principal,time and rate:")
p=int(input("principal:"))
t=int(input("time:"))
r=int(input("rate:"))
CI=p*pow((1+(r/100)),t)-p
print("the compound interest is :  ",CI)
