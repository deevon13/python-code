#Write a program to find largest of three numbers entered by the user. Use nestedif-else.

print("input three numbers:")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f"{a} is the largest number")
elif b>a and b>c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")