# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape:

    def Area(self):
        pass

    def Peri(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius * self.radius
    
    def Peri(self):
        return math.pi * 2 * self.radius
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width
    
    def Peri(self):
        return 2 * ( self.length + self.width)
    
class Triangle(Shape):

    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def Area(self):
        return 0.5 * self.base * self.height
    
    def Peri(self):
        return self.side1 + self.side2 + self.side3
    

r = 5
circle = Circle(r)
circle_area = circle.Area()
circle_peri = circle.Peri()

print("Radius of circle: ", r)
print("Area of circle: ", circle.Area())
print("Perimeter of circle: ", circle.Peri())

l = 7
w = 9
rect = Rectangle(l, w)
rect_area = rect.Area()
rect_peri = rect.Peri()

print("\nRectangle")
print("Length:", l, "  Width:", w)
print("Area of rectangle: ", rect.Area())
print("Perimeter of rectangle: ", rect.Peri())

b = 4
h = 3
s1 = 3
s2 = 4
s3 = 5
tri = Triangle(b, h, s1, s2, s3)
tri_area = tri.Area()
tri_peri = tri.Peri()
print("\nTriangle")
print("Base:", b, "  Height:", h, "  Side 1:", s1, "  Side 2:", s2, "  Side 3:", s3)
print("Area of triangle: ", tri.Area())
print("Perimeter of triangle: ", tri.Peri())