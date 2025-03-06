# 1. Program to print all even numbers from 0 to the entered number.

num = int(input("Enter a number: "))  # Taking input from the user

print("Even numbers from 0 to", num, "are:")
for i in range(0, num + 1, 2):  # Looping through even numbers with step 2
    print(i)


# 2. Program to print each character of a string on a new line.

user_string = input("Enter a string: ")  # Taking string input

print("Characters in the string:")
for char in user_string:  # Looping through each character in the string
    print(char)
