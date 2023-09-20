"""Wordle but only one shot"""
__author__ = "730657997"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"

guess: str = input("What is your 6-letter guess? ")

#program won't exit this loop until word is 6 characters long
while len(guess) != len(secret_word):
    guess = input("That was not 6 letters! Try again: ")

idx: int = 0
emojis: str = ""

#iterating thru each index
while idx < len(secret_word):
    #checking if character is an exact match
    if guess[idx] == secret_word[idx]:
        emojis = emojis + GREEN_BOX
    else:
        present: bool = False
        sub_idx: int = 0    
        #check if the guessed character is anywhere in the secret word
        while sub_idx < len(secret_word):
            if guess[idx] == secret_word[sub_idx]:
                present = True
            sub_idx += 1
        #if that character is in the word, turn it yellow, otherwise white
        if present == True:
            emojis = emojis + YELLOW_BOX
        else:
            emojis = emojis + WHITE_BOX
    idx += 1

#printing emojis and feedback
print(emojis)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")