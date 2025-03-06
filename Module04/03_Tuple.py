# 1. Create a tuple of your favorite foods and print the second food in the tuple.

foods = ("Pizza", "Biryani", "Pani Puri", "Chole Bhature", "Dosa")
print("Second food in the tuple:", foods[1])  # Index 1 gives the second food


# 2. Try to change the second food in the tuple and see what happens.

try:
    foods[1] = "Pasta"  # Tuples are immutable, so this will raise an error
except TypeError as e:
    print("Error:", e)


# 3. Create a new tuple that contains only the first and last foods in the original tuple and print it.

first_last_foods = (foods[0], foods[-1])  # Selecting the first and last foods
print("First and Last Food:", first_last_foods)


# 4. Use the len() function to find the number of foods in the tuple and print it.

print("Number of foods in the tuple:", len(foods))


# 5. Convert the tuple to a list and print the list.

foods_list = list(foods)  # Converting tuple to list
print("Tuple converted to list:", foods_list)
