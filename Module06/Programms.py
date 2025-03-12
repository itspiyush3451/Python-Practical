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




# 3. Count Vowels, Consonants, and Blanks in a String
def count_chars(s):
    vowels = "aeiouAEIOU"
    consonants = sum(1 for c in s if c.isalpha() and c not in vowels)
    vowel_count = sum(1 for c in s if c in vowels)
    blanks = s.count(' ')
    return vowel_count, consonants, blanks

# 4. Print Characters Common in Two Strings
def common_chars(s1, s2):
    return set(s1) & set(s2)

# 5. Calculate Percentage of Marks
def calculate_percentage(marks):
    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100
    return percentage

# 6. Display Fibonacci Sequence up to n Terms
def fibonacci(n):
    a, b = 0, 1
    fib_seq = []
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

# 7. Remove Duplicate Words from a Sentence and Sort Them
def remove_duplicates_sort(sentence):
    words = list(set(sentence.split()))
    return " ".join(sorted(words))

# 8. Implement Stack Operations using *args
def stack_operations(*args):
    stack = []
    for op in args:
        if op.startswith("push"):
            _, val = op.split()
            stack.append(val)
        elif op == "pop":
            if stack:
                stack.pop()
        elif op == "peek":
            if stack:
                return stack[-1]
    return stack

# Example Usage:
n = int(input("Enter a number: "))
print("Sum of even and odd numbers:", sum_odd_even(n))

s = input("Enter a string: ")
print("Is palindrome:", is_palindrome(s))

text = input("Enter a sentence: ")
print("Vowels, consonants, blanks:", count_chars(text))

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Common characters:", common_chars(s1, s2))

marks = list(map(int, input("Enter marks separated by space: ").split()))
print("Percentage:", calculate_percentage(marks))

n = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci sequence:", fibonacci(n))

sentence = input("Enter a sentence: ")
print("Sorted unique words:", remove_duplicates_sort(sentence))

operations = ["push 10", "push 20", "pop", "peek"]
print("Stack after operations:", stack_operations(*operations))