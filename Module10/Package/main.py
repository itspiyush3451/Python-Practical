# main.py - Using the 'library' package

# Importing the books module from the library package
from Library import books

# Importing the calculator module
import calculator

# List to store books
library_books = []

# Adding books
books.add_book(library_books, "Python Programming")
books.add_book(library_books, "Data Structures and Algorithms")
books.add_book(library_books, "Machine Learning Basics")

# Displaying books
books.display_books(library_books)

# Removing a book
books.remove_book(library_books, "Data Structures and Algorithms")

# Displaying books after removal
books.display_books(library_books)




# Using the calculator module 


# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
print(f"Addition: {calculator.add(num1, num2)}")
print(f"Subtraction: {calculator.subtract(num1, num2)}")
print(f"Multiplication: {calculator.multiply(num1, num2)}")
print(f"Division: {calculator.divide(num1, num2)}")