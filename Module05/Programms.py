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


#3. program to print the patterns

def pattern1(n):
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)))

def pattern2(n):
    for i in range(n):
        print(" ".join(chr(65 + j) for j in range(i + 1)))

def pattern3(n):
    for i in range(n, 0, -1):
        print(str(i) * i)

def pattern4(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

def pattern5(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (2 * i + 1))

def pattern6(n):
    for i in range(n):
        print("".join("01"[(i + j) % 2] for j in range(i + 1)))

def main():
    n = 5
    print("Pattern 1:")
    pattern1(n)
    print("\nPattern 2:")
    pattern2(n)
    print("\nPattern 3:")
    pattern3(n)
    print("\nPattern 4:")
    pattern4(n)
    print("\nPattern 5:")
    pattern5(n)
    print("\nPattern 6:")
    pattern6(n)

if __name__ == "__main__":
    main()








# Program to find ASCII value of a character
char = input("Enter a character: ")
if len(char) == 1:
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}")
else:
    print("Please enter a single character")






# Program to make a simple calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")





# Program to find the largest element in an array
def find_largest(arr):
    # Initialize maximum element
    max_element = arr[0]
    
    # Traverse array elements and compare with current max
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    
    return max_element

# Get input from user
size = int(input("Enter size of the array: "))
arr = []

for i in range(size):
    element = float(input(f"Enter element {i+1}: "))
    arr.append(element)

print(f"The largest element in the array is: {find_largest(arr)}")





# Program to add two matrices
def matrix_addition(X, Y):
    result = []
    for i in range(len(X)):
        row = []
        for j in range(len(X[0])):
            row.append(X[i][j] + Y[i][j])
        result.append(row)
    return result

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(element) for element in row))

# Get dimensions of matrices
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Initialize matrices
matrix1 = []
matrix2 = []

# Input for first matrix
print("\nEnter elements for first matrix:")
for i in range(rows):
    row = []
    for j in range(columns):
        element = float(input(f"Enter element at position ({i+1},{j+1}): "))
        row.append(element)
    matrix1.append(row)

# Input for second matrix
print("\nEnter elements for second matrix:")
for i in range(rows):
    row = []
    for j in range(columns):
        element = float(input(f"Enter element at position ({i+1},{j+1}): "))
        row.append(element)
    matrix2.append(row)

# Add matrices and display result
result = matrix_addition(matrix1, matrix2)

print("\nFirst Matrix:")
print_matrix(matrix1)

print("\nSecond Matrix:")
print_matrix(matrix2)

print("\nResult after addition:")
print_matrix(result)