import re

# Sample text for demonstration
text = "The event was held on 2023-08-15. There were 123 guests, 45 volunteers, and 789 supporters."

# 1. Extract year, month, and date from a string
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"  # Pattern to match YYYY-MM-DD format
match = re.search(date_pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Date: {day}")

# 2. Extract only 3-digit numbers from the string
three_digit_numbers = re.findall(r"\b\d{3}\b", text)  # \b ensures exact match of three-digit numbers
print("Three-digit numbers:", three_digit_numbers)

# 3. Extract all words and numbers from the string
words_and_numbers = re.findall(r"\w+", text)  # \w+ matches words and numbers
print("Words and numbers:", words_and_numbers)

# 4. Find all words that start with a vowel (A, E, I, O, U)
vowel_words = re.findall(r"\b[aeiouAEIOU]\w*", text)  # Matches words that start with vowels
print("Words starting with a vowel:", vowel_words)

# 5. Find all words that start with a consonant
consonant_words = re.findall(r"\b[^aeiouAEIOU\s\d]\w*", text)  # Excludes vowels, digits, and spaces
print("Words starting with a consonant:", consonant_words)

# 6. Count occurrences of "a", "an", and "the" (case-insensitive)
article_count = len(re.findall(r"\b(a|an|the)\b", text, re.IGNORECASE))  # \b ensures full word match
print("Total occurrences of 'a', 'an', and 'the':", article_count)
