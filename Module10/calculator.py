# A module in Python is simply a .py file that contains functions.
# calculator.py - A module to perform simple calculator operations

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division (handling division by zero)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b
