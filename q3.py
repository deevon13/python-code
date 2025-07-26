#Write a program with classes to represent a circle, rectangle, and triangle. Each class should have data members to represent the actual objects and member functions to read and display objects, find perimeter and area of the objects, and other useful functions. Use the classes to create objects in your program.

class Circle:
    def __init__ (self):
        self.radius = float(input("Enter the radius of the circle: "))
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle:
    def __init__(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle:
    def __init__(self):
        self.side1 = float(input("Enter the length of side 1: "))
        self.side2 = float(input("Enter the length of side 2: "))
        self.side3 = float(input("Enter the length of side 3: "))
    def area(self):  
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    print("Choose a shape to calculate area and perimeter:")
print("1. Circle\n2. Rectangle\n3. Triangle")
choice = int(input("Enter your choice (1/2/3): "))
if choice == 1: 
    c=Circle()
    print("Area of the circle:", c.area())
    print("Perimeter of the circle:", c.perimeter())
elif choice == 2:   
    r=Rectangle()
    print("Area of the rectangle:", r.area())
    print("Perimeter of the rectangle:", r.perimeter())
elif choice == 3:
    t=Triangle()
    print("Area of the triangle:", t.area())
    print("Perimeter of the triangle:", t.perimeter())
else:
    print("Invalid choice. Please select 1, 2, or 3.")
    

  