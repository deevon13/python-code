#Write a program to read annual salary of an employee and decide the tax to be deducted according to following scheme:
# up to Rs. 400,000 – 1%
# Rs. 400,000 to Rs. 500,000 – 10%
# Rs. 500,000 to Rs. 700,000 – 20%
# Above Rs. 700,000 – 30%




sal=int(input("Enter the salary:"))
if sal<400000:
    tax=sal*0.01
    print("tax amount is :",tax)
elif sal>=400000 and sal<500000:
    tax=sal*0.1
    print("tax amount is :",tax)
elif sal>=500000 and sal<700000:
    tax=sal*0.2
    print("tax amount is :",tax)
