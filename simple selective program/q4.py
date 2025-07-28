#Write a program to read two floating point numbers and find their ratio. If the ratio is less than 1 swap the numbers and find the ratio again.

print("enter two floating numbers:")
a=float(input("a:"))
b=float(input("b:"))
rat=a/b
if rat>1:
    print("the ratio is :",rat)
elif rat<1:
    rat=b/a
    print("the ration is :",rat)    