import sys
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount      
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
            sys.exit()
        else:    
            self.balance -= amount
            print("******withdrawn successfully*******")      
    def status(self):
        print("\n\n\tPRABHU BANK LIMITED\n")
        print("Account holder:", self.name)
        print("Current balance: Rs", self.balance)        
print("\t PRABHU BANK LIMITED \t\nWELCOME TO THE MOBILE BANKING SYSTEM\n\n")
name=input("Enter your name: ")
b=Bank(name,1000.0)
print("Hello", name, "!")
print("Your account balance is:Rs ",b.balance)
print("\nPlease select an option\n1.W for withdraw\n2.D for deposit:\n3.S for status\n4.E for exit")
option = input("Enter your option: ")
if option == 'W' or option == 'w':
    amount = float(input("Enter the amount to withdraw: "))
    b.withdraw(amount)
elif option == 'D' or option == 'd':
    amount = float(input("Enter the amount to deposit: "))
    b.deposit(amount)
elif option == 'S' or option == 's':
    b.status()
elif option == 'E' or option == 'e':
    print("Exiting the system. Thank you!")
    sys.exit()
    
else:
    print("Invalid option selected.")
b.status()
print("Thank you for using our service!")
    

    