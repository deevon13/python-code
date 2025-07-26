def largest(n):
    digit=[int(x) for x in str(n)] #splitting the number into its digits by converting to string and making a list
    print("The digit is:", digit)
    max=0
    for i in digit:
        if i > max:
            max = i
    print("The largest digit is:", max)
n=int(input("enter the integers(greater than one digit):"))
largest(n)