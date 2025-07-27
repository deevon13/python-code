#Write a program to check whether the given number is even and positive or else
a=int(input("enter a number:"))
if a%2==0 and a>0:
    print("even and positive number")
elif a%2==0 and a<0:
    print("even and negative number")
elif a%2!=0 and a>0:
    print("odd and positive number")
elif a%2!=0 and a<0:
    print("odd and negative number")   