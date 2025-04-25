class Circle:

    def __init__(self, red):
        self.red = red

    def Area(self):
        return 3.14 * self.red * self.red

    def Peri(self):
        return 2 * 3.14 * self.red

r = float(input("Enter the radius of Cicle: "))
c = Circle(r)

print("Area of circle: ",c.Area())
print("Perimeter of circle: ",c.Peri())