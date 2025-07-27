#Write a program to check if the number is divisible by 3 and not by 5

a=int(input("enter a number:"))
if(a%3==0 and a%5!=0) or (a%3==0 and a%5==0):
    print(f"{a} is divisible by 3")
elif a%5==0 and a%3!=0:
    print(f"{a} is divisible by 5 ")