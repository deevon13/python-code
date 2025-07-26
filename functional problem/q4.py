#Write a program to calculate the sum of the following series using function. Read the value of x and n and pass it to the function, which calculates the sum, and return the value.
      # sum= 1 + 1/x + 1/x^2 + 1/x^3 + ... + 1/x^n

from math import pow
def sum(x,n):
    sum=0
    for i in range(1,n+1):
        sum+=1/pow(x,i)
    return(sum+1)
x=int(input("enter the value of x:"))
n=int(input("enter the value of n:"))
print("The sum of the series is:",sum(x,n))


