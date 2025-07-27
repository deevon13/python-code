#Write a program to read two numbers and subtract smaller from larger
print("Enter two numbers:")
a = int(input("a: "))
b = int(input("b: "))
if a > b:
    sub=a-b
    print("the substraction is:",sub)
else:
    sub=b-a
    print("the substraction is:",sub)
