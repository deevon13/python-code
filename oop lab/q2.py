#Write a program that represent a box class with attributes length, width, and height Add methods that return volume and base area and surface area of thebox.

class Box:
    def __init__ (self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height

    def volume(self):
        return self.length * self.breadth * self.height

    def base_area(self):
        return self.length * self.breadth

    def surface_area(self):
        return 2 * (self.length * self.breadth + self.length * self.height + self.breadth * self.height)    
a = float(input("Enter length of the box: "))
b = float(input("Enter width of the box: "))
c = float(input("Enter height of the box: "))    
b=Box(a,b,c)
print("the area of the box is:",b.base_area())
print("the volume of the box is:",b.volume())
print("the surface area of the box is:",b.surface_area())