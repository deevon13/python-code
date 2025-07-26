# Write a program with a function that checks whether the year passed to it is a leap year or not. The function should return true (1) if the year is leap year and false (0) if not leap year. Display the result in the calling function def leap(n):
 
def leap(n):  
    if(n%4==0 and n%100!=0) or (n%400==0):
        return True
    else:
        return False
n=int(input("enter the year:"))
print("is this a leap year?")
print(leap(n))
