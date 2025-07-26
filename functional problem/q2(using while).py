
def largest(n):
    max = 0
    while n!=0: #splitting the number into its digits using while loop
        r=n%10
        if r > max:
            max = r
            return max
        n=n//10
n=int(input("enter the integers(greater than one digit):"))
print("The largest digit is:",largest(n))    
