class StudentDetails:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}")
name = str(input("Enter the name of the student: "))
age = int(input("Enter the age of the student: "))
roll_number = int(input("Enter the roll number of the student: "))
result = StudentDetails(name, age, roll_number)
result.display()
