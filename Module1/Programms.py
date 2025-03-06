# 1. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output: r = 1.1  Area = 3.8013271108436504

import math  # Importing the math module for using pi

radius = float(input("Enter the radius of the circle: "))  # Taking input from the user
area = math.pi * (radius ** 2)  # Formula for area of circle: πr²
print(f"r = {radius}  Area = {area}")  # Displaying the result


# 2. Write a Python program that accepts the user's first and last name 
# and prints them in reverse order with a space between them.

first_name = input("Enter your first name: ")  # Taking first name as input
last_name = input("Enter your last name: ")  # Taking last name as input
print(last_name + " " + first_name)  # Printing names in reverse order


# 3. Write a Python program that accepts a sequence of comma-separated numbers from the user
# and generates a list and a tuple of those numbers.

numbers = input("Enter comma-separated numbers: ")  # Taking input as a string
num_list = numbers.split(",")  # Splitting string into list elements
num_tuple = tuple(num_list)  # Converting list to tuple
print("List:", num_list)  # Printing list
print("Tuple:", num_tuple)  # Printing tuple


# 4. Write a Python program that determines whether a given number (accepted from the user) 
# is even or odd, and prints an appropriate message to the user.

num = int(input("Enter a number: "))  # Taking number input
if num % 2 == 0:  # Checking divisibility by 2
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")


# 5. Write a Python program to concatenate N strings.

n = int(input("Enter the number of strings you want to concatenate: "))  # Taking count of strings
concatenated_string = ""  # Initializing empty string
for _ in range(n):  # Loop runs n times
    user_string = input("Enter a string: ")  # Taking input string
    concatenated_string += user_string  # Concatenating strings
print("Concatenated String:", concatenated_string)  # Printing the final concatenated result
