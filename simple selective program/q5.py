#Write a program to find whether the number is positive, negative or zero 

a=int(input("Enter a number:"))
if a>0:
    print(f"{a} is positive number")
elif a<0:
    print(f"{a} is negative number")
else:
    print("it is zero")
    