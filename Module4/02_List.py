# 1. Create a list of your favorite Hindi comedy movies and print the third movie in the list.

movies = ["Hera Pheri", "Andaz Apna Apna", "Dhamaal", "Chup Chup Ke", "Golmaal: Fun Unlimited"]
print("Third movie in the list:", movies[2])  # Index 2 gives the third movie


# 2. Add a new movie to the list and print the updated list.

movies.append("Bhool Bhulaiyaa")  # Adding a new movie to the list
print("Updated Movie List:", movies)


# 3. Remove the second movie from the list and print the updated list.

movies.pop(1)  # Removing the second movie (index 1)
print("List after removing the second movie:", movies)


# 4. Sort the list in alphabetical order and print the sorted list.

movies.sort()  # Sorting the list alphabetically
print("Sorted Movie List:", movies)


# 5. Create a new list that contains only the first and last movie in the original list and print it.

first_last_movies = [movies[0], movies[-1]]  # Selecting the first and last movies
print("First and Last Movie:", first_last_movies)
