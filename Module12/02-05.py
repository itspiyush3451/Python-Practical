import re

# 2. Find all words which are at least 4 characters long in a string
def find_long_words(text):
    long_words = re.findall(r"\b\w{4,}\b", text)  # Matches words with 4 or more characters
    return long_words

# 3. Check for a number at the end of a string
def check_number_at_end(text):
    return bool(re.search(r"\d+$", text))  # Checks if a number is at the end of the string

# 4. Check for a number starting with 2 or 1 and having exactly 4 digits
def check_four_digit_number(text):
    return bool(re.search(r"\b[12]\d{3}\b", text))  # Matches 4-digit numbers starting with 1 or 2

# 5. Match a string that has an 'a' followed by anything, ending in 'b'
def match_a_anything_b(text):
    return bool(re.fullmatch(r"a.*b", text))  # Matches strings that start with 'a' and end with 'b'

# Sample test cases
sample_text = "This is a simple example with words like apple, banana, and 2023."
print("Words with at least 4 characters:", find_long_words(sample_text))

sample_text2 = "The final number is 1234"
print("Number at the end of the string:", check_number_at_end(sample_text2))

sample_text3 = "The year is 2024"
print("Four-digit number starting with 1 or 2:", check_four_digit_number(sample_text3))

sample_text4 = "ab"
print("Matches 'a' followed by anything, ending in 'b':", match_a_anything_b(sample_text4))


# Explanation : 
# Find words with at least 4 characters → Uses \b\w{4,}\b to find words of at least 4 letters.
# Check for a number at the end of a string → Uses \d+$ to check if the string ends with a number.
# Check for a number starting with 2 or 1 and having exactly 4 digits → Uses \b[12]\d{3}\b to match numbers like 1234 or 2024.
# Match 'a' followed by anything, ending in 'b' → Uses a.*b to match patterns like "ab", "acb", "axyzb".