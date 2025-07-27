#Write a program to read two numbers and find the sum, difference, product and quotient of those numbers. Ask for the operand character (+, -, *, /) and find the result for different cases using else if statement

print("CHOOSE THE OPERATION(1,2,3)\n1.addition(+)\n2.substraction(-)\n3.division(/)\n4.multiplication:")
ch=input()
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if ch=='1':
    sum=a+b
    print("the sum is\n:",sum)
elif ch=='2':
    sub=a-b
    print("the difference is:\n",sub)
elif ch=='3':  
    div=a/b
    print("the division is:\n",div)
else:
    mul=a*b
    print("the multiplication is:\n",mul)


