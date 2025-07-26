def rev(n):
    num=0
    while n!=0:
        rem=n%10
        num=num*10+rem
        n=n//10
    return num    
n=int(input("enter the integers(greater than one digit):"))
print("The reverse of the number is:", rev(n))