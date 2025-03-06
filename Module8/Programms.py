# 1. Program to Read marks from user and Find the percentage of marks of student.

def calculate_percentage(marks, total_marks):
    return (sum(marks) / total_marks) * 100  # Calculating percentage

# Taking input from the user
num_subjects = int(input("Enter the number of subjects: "))
marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total_marks = num_subjects * 100  # Assuming each subject is out of 100
percentage = calculate_percentage(marks, total_marks)

print(f"Student's percentage: {percentage:.2f}%")


# 2. Function to Display the Fibonacci Sequence up to nth Term.

def fibonacci(n):
    fib_sequence = [0, 1]  # Starting the sequence with first two numbers
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Adding last two numbers
    return fib_sequence[:n]  # Returning the sequence up to n terms

# Taking input from the user
n_terms = int(input("Enter the number of terms for Fibonacci sequence: "))

if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Sequence:", fibonacci(n_terms))
