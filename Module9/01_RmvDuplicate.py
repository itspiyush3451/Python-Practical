# 1. Function to remove duplicate words from a sentence and print sorted unique words.

def remove_duplicates_and_sort(sentence):
    words = sentence.split()  # Splitting sentence into a list of words
    unique_words = sorted(set(words))  # Removing duplicates using set and sorting the words
    return " ".join(unique_words)  # Joining the sorted unique words back into a string

# Taking input from the user
user_sentence = input("Enter a sentence: ")

# Calling the function and printing the result
result = remove_duplicates_and_sort(user_sentence)
print("Sorted unique words:", result)