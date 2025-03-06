# 1. Program to Find the GCD of Two Positive Numbers.

import math  # Importing math module to use gcd function

num1 = int(input("Enter first positive number: "))  
num2 = int(input("Enter second positive number: "))  

gcd = math.gcd(num1, num2)  # Using built-in gcd function
print(f"GCD of {num1} and {num2} is {gcd}")


# 2. Write Python Program to Find the Sum of Digits in a Number.

num = int(input("Enter a number: "))  # Taking input
sum_of_digits = sum(int(digit) for digit in str(abs(num)))  # Convert number to string, iterate, convert back to int, and sum
print(f"Sum of digits in {num} is {sum_of_digits}")


# 3. Write a program that prints the first 10 multiples of 3.

multiples_of_3 = [3 * i for i in range(1, 11)]  # Generating multiples using list comprehension
print("First 10 multiples of 3:", multiples_of_3)
