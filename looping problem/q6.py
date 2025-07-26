x=int(input("ENTER THE DIGIT:"))
digit=[int(i) for i in str(x)]
sum=0
for i in digit:
    sum+=i
print("The sum of digits is", sum)