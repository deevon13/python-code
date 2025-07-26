#Write a program with a class that represent number with attribute number. Add methods to check whether the number is even/odd, positive/negative or prime. You should ask for numbers repeatedly. When it finishes checking a number the program asks if the user wants to do another calculation. The response can be ’y’ or ’n’. Don’t forget to use the object-oriented concept




class Check:
    def __init__(self,number):
        self.number=number 
    def  odd_even(self):
        if self.number%2==0:
            print("The number is even")
        else:
            print("The number is odd")
    def pos_neg(self):
        if self.number>0:
            print("The number is positive")
        elif self.number<0:
            print("The number is negative")
        else:
            print("The number is zero")
    def prime(self):
        if self.number > 1:
            for i in range(2, int(self.number ** 0.5) + 1):
                if (self.number % i) == 0:
                    print("The number is not prime")
                    break
            else:
                print("The number is prime")
        else:
            print("The number is not prime") 
    def display(self):
        self.odd_even()
        self.pos_neg()
        self.prime()      
ch='y'
while ch=='y':
    
    number=int(input("Enter the number :"))
    c=Check(number)
    c.display()
    ch=input("Do you want to continue? (y/n): ")
else:
    print("Thank you for using the program!")
