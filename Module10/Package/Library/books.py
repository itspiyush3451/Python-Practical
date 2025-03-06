# books.py - A module inside the 'library' package

# Function to add a book to the library system
def add_book(book_list, book_name):
    book_list.append(book_name)
    print(f'Book "{book_name}" added successfully!')

# Function to remove a book from the library system
def remove_book(book_list, book_name):
    if book_name in book_list:
        book_list.remove(book_name)
        print(f'Book "{book_name}" removed successfully!')
    else:
        print(f'Book "{book_name}" not found in the library!')

# Function to display all available books
def display_books(book_list):
    if book_list:
        print("Available Books in the Library:")
        for book in book_list:
            print(f"- {book}")
    else:
        print("No books available in the library!")
