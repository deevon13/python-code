#Write a program to read a character and check whether it is vowel or consonant and upper case or lower case.

a=input("enter the alphabet:")
if a.isalpha():
    s=a.lower()
    if s in 'aeiou':
        print(f"{a} is a vowel")
    else:
        print(f"{a} is a consonant")
else:
    print("Please enter a valid alphabet")
        
