# 1. Create a dictionary of your favorite books and their authors and print it.

books = {
    "1984": "George Orwell",
    "To Kill a Mockingbird": "Harper Lee",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen"
}

print("Favorite Books and Authors:", books)


# 2. Add a new book to the dictionary and print the updated dictionary.

books["The Catcher in the Rye"] = "J.D. Salinger"  # Adding a new book
print("Updated Books Dictionary:", books)


# 3. Remove a book from the dictionary and print the updated dictionary.

books.pop("1984")  # Removing a book by title
print("Dictionary after removing a book:", books)


# 4. Use the keys() method to print a list of the book titles in the dictionary.

print("Book Titles:", list(books.keys()))  # Extracting only book titles


# 5. Use the values() method to print a list of the author names in the dictionary.

print("Author Names:", list(books.values()))  # Extracting only author names


# 6. Create a set of your favorite colors and print it.

colors = {"Red", "Blue", "Green", "Black", "White"}
print("Favorite Colors Set:", colors)


# 7. Add a new color to the set and print the updated set.

colors.add("Yellow")  # Adding a new color
print("Updated Colors Set:", colors)


# 8. Remove a color from the set and print the updated set.

colors.discard("White")  # Removing a color
print("Set after removing a color:", colors)


# 9. Create a new set that contains only the colors that start with the letter "B" and print it.

colors_starting_with_B = {color for color in colors if color.startswith("B")}
print("Colors starting with 'B':", colors_starting_with_B)


# 10. Use the len() function to find the number of colors in the set and print it.

print("Number of colors in the set:", len(colors))
