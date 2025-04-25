# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date

class Person:

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def Age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age
    
per1 = Person("Darshil", "India", date(2004, 7, 8))
per2 = Person("Juhil", "India", date(2008, 12, 4))
per3 = Person("Om", "India", date(2004, 4, 25))

print("Person 1: ")
print("Name: ", per1.name)
print("Country: ", per1.country)
print("Date of Birth: ", per1.dob)
print("Age: ", per1.Age())

print("Person 2: ")
print("Name: ", per2.name)
print("Country: ", per2.country)
print("Date of Birth: ", per2.dob)
print("Age: ", per2.Age())

print("Person 3: ")
print("Name: ", per3.name)
print("Country: ", per3.country)
print("Date of Birth: ", per3.dob)
print("Age: ", per3.Age())