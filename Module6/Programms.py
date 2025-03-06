# 1. Program to find the sum of all odd and even numbers up to a number specified by the user.

def sum_odd_even(n):
    even_sum = sum(i for i in range(0, n+1, 2))  # Sum of even numbers
    odd_sum = sum(i for i in range(1, n+1, 2))  # Sum of odd numbers
    return even_sum, odd_sum

num = int(input("Enter a number: "))  # Taking input from the user
even_sum, odd_sum = sum_odd_even(num)  # Calling the function

print(f"Sum of even numbers up to {num} is: {even_sum}")
print(f"Sum of odd numbers up to {num} is: {odd_sum}")


# 2. Program to check if a given string is a palindrome using slicing.

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Converting to lowercase and removing spaces
    return s == s[::-1]  # Checking if the string is equal to its reverse

user_string = input("Enter a string: ")  # Taking input from the user

if is_palindrome(user_string):  # Checking if palindrome
    print(f"'{user_string}' is a palindrome.")
else:
    print(f"'{user_string}' is not a palindrome.")
