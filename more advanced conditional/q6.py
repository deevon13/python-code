#Write a program to check the eligibility of a candidate for examination. The eligibility is the candidate should be minimum 22 years and should pass bachelor’s degree. Use nested if-else.

age=int(input("Enter your age: "))
degree=input("Enter your bachelor degree\np for pass\nf for fail\nchoose: ")
l=degree.lower()
if age>=22 and l=='p':
    print("You are eligible for the exam")
else:
    print("You are not eligible for the exam")
