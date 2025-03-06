# 1. Write a Python program to do arithmetical operations addition and division.

a = float(input("Enter first number: "))  # Taking first input
b = float(input("Enter second number: "))  # Taking second input

addition = a + b  # Performing addition
division = a / b if b != 0 else "Undefined (division by zero)"  # Checking division by zero

print("Addition:", addition)
print("Division:", division)


# 2. Write a Python program to find the area of a triangle.

base = float(input("Enter base of the triangle: "))  # Taking base as input
height = float(input("Enter height of the triangle: "))  # Taking height as input
area = 0.5 * base * height  # Formula for area of triangle: (1/2) * base * height
print("Area of the triangle:", area)


# 3. Write a Python program to swap two variables.

x = input("Enter first variable: ")  
y = input("Enter second variable: ")

x, y = y, x  # Swapping values

print("After swapping: x =", x, "y =", y)


# 4. Write a Python program to generate a random number.

import random  # Importing random module

rand_num = random.randint(1, 100)  # Generating a random number between 1 and 100
print("Random number:", rand_num)


# 5. Write a Python program to convert kilometers to miles.

km = float(input("Enter distance in kilometers: "))  # Taking input in kilometers
miles = km * 0.621371  # Conversion formula
print(f"{km} kilometers is equal to {miles} miles")


# 6. Write a Python program to display calendar.

import calendar  # Importing calendar module

year = int(input("Enter year: "))  # Taking year input
month = int(input("Enter month (1-12): "))  # Taking month input

print(calendar.month(year, month))  # Displaying calendar for given month and year


# 7. Write a Python program to swap two variables without temp variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b  # Step 1: Sum of both numbers is stored in 'a'
b = a - b  # Step 2: 'b' is assigned the value of 'a - b' (original value of 'a')
a = a - b  # Step 3: 'a' is assigned the value of 'a - b' (original value of 'b')

print("After swapping: a =", a, "b =", b)


# 8. Write a Python program to check if a number is positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# 9. Write a Python program to check if a year is a leap year.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# 10. Write a Python program to check if a number is odd or even.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
