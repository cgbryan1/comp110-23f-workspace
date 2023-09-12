"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730657997"
full_word: str = input("Enter a 5-character word: ")

if (len(full_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

one_char: str = input("Enter a single character: ")

if (len(one_char) != 1):
    print("Error: Character must be a single character ")
    exit()

print("Searching for " + one_char + " in " + full_word)

counter: int = 0

if (full_word[0]) == one_char:
    print(one_char + " found at index 0")
    counter += 1 
if (full_word[1]) == one_char:
    print(one_char + " found at index 1")
    counter += 1 
if (full_word[2]) == one_char:
    print(one_char + " found at index 2")
    counter += 1 
if (full_word[3]) == one_char:
    print(one_char + " found at index 3")
    counter += 1 
if (full_word[4]) == one_char:
    print(one_char + " found at index 4")
    counter += 1 

if (counter == 0):
    print("No instances of " + one_char + " found in " + full_word)
elif (counter == 1):
    print("1 instance of " + one_char + " found in " + full_word)
else:
    print(str(counter) + " instances of " + one_char + " found in " + full_word)