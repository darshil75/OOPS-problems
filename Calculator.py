# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:

    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y
    
    def mul(self, x, y):
        return x * y
    
    def div(self, x, y):
        if y != 0:
            return x / y
        else:
            print("Cannot divide by Zero")

calculator = Calculator()

result = calculator.add(10, 15)
print("10 + 15 = ", result)

result = calculator.sub(100, 40)
print("100 - 40 = ", result)

result = calculator.mul(10, 6)
print("10 * 6 = ", result)

result = calculator.div(225, 5)
print("225 / 5 = ", result)

result = calculator.div(36, 0)
print("36 / 0 = ", result)
