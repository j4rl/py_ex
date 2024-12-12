# Commenting in Python
In Python, comments are used to explain the code and make it more readable. They are ignored by the interpreter when the code is executed. There are two ways to write comments in Python:
## What my comment should be
- Single-line comments: These comments start with a hash symbol (#) and continue until the end of the line. They are used to explain a single line of code.
- Multi-line comments: These comments start and end with three single quotes (''') or three double quotes ("""). They are used to explain multiple lines of code.
## What should i write in my comment
When writing comments, it is important to keep them concise and to the point. Comments should explain why the code is written in a certain way, not what the code does. They should also be written in clear and simple language so that anyone reading the code can understand them. Your comment should explain WHY you wrote the code, not WHAT the code does.
Here are some examples of good comments:
- `# This code calculates the sum of two numbers becaase otherwise the function will not work`
- `# This code checks if a number is greater than 5, if it's larger, memory will be full` 
- `# This code loops through a list of numbers and places them in a new list for sorting`
Here are some examples of bad comments:
## When should i comment my code
You should comment your code whenever you think it is necessary to explain what the code does or why it is written in a certain way. Comments are especially useful when the code is complex or when it is not immediately obvious what the code is doing.
## Example
Here is an example of how to use comments in Python:
```python
# This is a single-line comment
print("Hello, World!") # This is another single-line comment

'''
This is a multi-line comment
It can span multiple lines
'''
print("Hello, World!")
```
In this example, the comments explain what the code does and why it is written in a certain way. They make the code more readable and easier to understand.
## Header comments for functions and classes
When writing functions and classes, it is a good idea to include a header comment that explains what the function or class does.  
Here is an example:
```python
###############################################
#  Name: add                                  #
#  Parameters: a, b                           #
#  Returns: The sum of a and b                #
#  Description:This function adds two numbers #
#  and returns the result                     #
###############################################
def add(a, b):
    return a + b
```
...or you can use the docstring to write a comment for the function:
```python
def add(a, b):
    """
    This function adds two numbers and returns the result
    """
    return a + b
```
In this example, the docstring explains what the `add` function does. It makes it clear to anyone reading the code what the function is supposed to do.
**The first example is superior because it is more readable and easier to understand.** 

## Comments for debugging
Comments can also be used for debugging purposes. You can use comments to temporarily disable a piece of code or to add debugging information to the code. Here is an example:
```python
# This code is not working, need to fix it
# print("Hello, World!")
```

## Conclusion
Comments are an important part of writing clean and readable code. They help explain the code and make it easier to understand. By using comments effectively, you can make your code more maintainable and easier to work with.