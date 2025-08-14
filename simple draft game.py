from random import *
class ludo:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def draft(self):
        print("Your choice is:",self.a)
        print("Random number is:",self.b)
        if self.a==self.b:
            print("congratulations! You have won the game")
        else:
            print("oops!out of luck")        

print("welcome to draft game/nrules of the game:\n1. you have to choose a number between 1-5\n2. a random number will be generated between 1-6\n3. if your choice matches the random number, you win\n4. otherwise, you lose")
ch='y'
while ch=='y':
    print("PLEASE PLAY! \n")
    a=int(input("Enter your choice(1-5):"))
    b=randint(1,6)
    l=ludo(a,b)
    l.draft()
    ch=input("do you want to play again? (y/n):")
else:
    print("Thank you for playing the game")    







