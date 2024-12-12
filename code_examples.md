# Here are som fundamental code examples in Python
## Variables and Types
In this example we will see how to declare variables and their types in Python.
```python
# Declare a variable
a = 10
b = "Hello, World!"
c = 3.14
d = True
print(a, b, c, d)
```
## Conditions
In this example we will see how to use conditions in Python.
```python
# Declare a variable
a = 10
# Check if a is greater than 5
if a > 5:
    print("a is greater than 5")
else:
    print("a is not greater than 5")
```
## Loops
In this example we will see how to use loops in Python.
```python
# Declare a variable
a = 10
# Loop from 0 to 10
for i in range(a):
    print(i)
# simple while loop
i = 0
while i < a:
    print(i)
    i += 1
# Loop through a list
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)
```
## Functions
In this example we will see how to declare and use functions in Python.
```python
# Declare a function
def add(a, b):
    return a + b
# Call the function
result = add(10, 20)
print(result)
```
## Example how to make a menu in python
In this example we will see how to make a simple menu in Python.
```python
# Declare a function
def menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

# Call the function
choice = menu()
print("You chose option", choice)
```

