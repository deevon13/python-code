def rev(n):
    num=str(n)[::-1]  # Reversing the number by converting to string and slicing
    return int(num)  
n=int(input("enter the integers(greater than one digit):"))
print("the reverse is :",rev(n))
