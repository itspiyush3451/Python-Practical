# 1. Function to count the total number of vowels, consonants, and blanks in a string.

def count_vowels_consonants_blanks(s):
    vowels = "aeiouAEIOU"
    consonants_count = vowels_count = blanks_count = 0

    for char in s:
        if char in vowels:  
            vowels_count += 1  # Counting vowels
        elif char.isalpha():  
            consonants_count += 1  # Counting consonants (letters that are not vowels)
        elif char.isspace():  
            blanks_count += 1  # Counting blank spaces

    return vowels_count, consonants_count, blanks_count

# Taking input from the user
user_string = input("Enter a string: ")
vowels, consonants, blanks = count_vowels_consonants_blanks(user_string)

print(f"Vowels: {vowels}, Consonants: {consonants}, Blanks: {blanks}")


# 2. Function to print characters that are common in two strings.

def common_characters(str1, str2):
    common_chars = set(str1) & set(str2)  # Finding common characters using set intersection
    return "".join(sorted(common_chars))  # Returning sorted common characters as a string

# Taking input for two strings
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

common_chars = common_characters(string1, string2)
print(f"Common characters: {common_chars}" if common_chars else "No common characters found.")
