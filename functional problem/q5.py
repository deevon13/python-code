# sum of series 1/1! + 1/2! + 1/3! + ... + 1/n!
# where n is the input from the user


def fact(i):
    f=1
    for j in range(1,i+1):
        f=f*j
    return f
def sum(x):
    sum=0
    for i in range(1,x+1):
        sum+=1/fact(i)
    return sum
x=int(input("enter the value of x:"))   
print("The sum of the series is:", sum(x))



         