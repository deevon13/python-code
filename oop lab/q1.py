 #Write a program to make a class that represent a person and add attributes that
#represent name, age, phone number and address. Add methods required for object
#manipulation.

class Person:
    def __init__(self,name, age, phone_number, address):
        self.name =name
        self.age = age
        self.phone_number = phone_number
        self.address = address

    def update_phone(self, new_phone):
        self.phone_number = new_phone
        print("Phone number updated to:", self.phone_number)

    def update_address(self, new_address):
        self.address = new_address
        print("Address updated to:", self.address)

    def birthday(self):
        self.age += 1
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("phone number:", self.phone_number)
        print("address:", self.address)


p=Person("rahul",21,9843293954,"kathmandu")
p.display()
p.update_phone(9843293955)
p.update_address("lalitpur")
p.birthday()
p.display()