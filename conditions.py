# Example of different conditional statements

# If statement
x = 10
if x > 0:
    print("x is positive")

# If-else statement
y = -5
if y > 0:
    print("y is positive")
else:
    print("y is non-positive")

# If-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")

# Nested if statement
a = 15
if a > 0:
    if a % 2 == 0:
        print("a is a positive even number")
    else:
        print("a is a positive odd number")
else:
    print("a is non-positive")

# Ternary operator
b = 7
result = "Even" if b % 2 == 0 else "Odd"
print(f"b is {result}")

# Switch-case-like behavior using dictionary
day = "Monday"
actions = {
    "Monday": "Go to work",
    "Tuesday": "Attend meetings",
    "Wednesday": "Work on projects",
    "Thursday": "Review progress",
    "Friday": "Prepare for the weekend",
    "Saturday": "Relax and have fun",
    "Sunday": "Rest and recharge"
}
print(actions.get(day, "Invalid day"))

# Membership operator
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("3 is present in the list")

# Comparison operator
num1 = 10
num2 = 20
if num1 != num2:
    print("num1 and num2 are not equal")

# Logical operators
p = True
q = False
if p and not q:
    print("p is true and q is false")

# Short-circuit evaluation
r = 5
if r > 0 or r / 0 > 0:
    print("r is positive or division by zero occurred")