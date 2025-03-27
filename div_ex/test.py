# Variable declaration
name = "John"
age = 25
is_student = True

# Iteration using for loop
for i in range(5):
    print("Iteration", i)

# Iteration using while loop
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1

# Conditional statements
if age >= 18:
    print(name, "is an adult.")
else:
    print(name, "is a minor.")

if is_student:
    print(name, "is a student.")
else:
    print(name, "is not a student.")

# Function to calculate the square of a number
def square(num):
    return num ** 2

# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example of input from the user
user_input = input("Enter a number: ")
number = int(user_input)

# Calling the square function and printing the result
result = square(number)
print("Square of", number, "is", result)

# Calling the check_even_odd function and printing the result
result = check_even_odd(number)
print(number, "is", result)

# Class example
class Person:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        if self.is_student:
            print("Student: Yes")
        else:
            print("Student: No")

# Creating an instance of the Person class
person = Person(name, age, is_student)

# Calling the display_info method of the person object
person.display_info()