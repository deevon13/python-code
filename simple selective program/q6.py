#Write a program to find the sum of digits of a four-digit integer number

a=int(input("enter four digit number:"))
digit=[int(x) for x in str(a)]
print(type(digit))
sum=0
for y in digit:
    sum=sum + y
print("the sum is :",sum)





