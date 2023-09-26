"""Real wordle!!!"""
__author__ = "730657997"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, char: str) -> bool:
    """Checks to see if character is included in string"""
    assert len(char) == 1
    idx: int = 0

    while (idx < len(word)):
        # check if the guess is right
        if (word[idx] == char):
            return True
        # otherwise, decision will remain false
        idx +=1

    return False

def emojified(guess: str, secret: str) -> str:
    """returns an emoji string!"""
    assert len(guess) == len(secret)
    emojis: str = ""
    idx: int = 0

    while idx < len(guess):
        # green if letter is in right spot
        if guess[idx] == secret[idx]:
            emojis += GREEN_BOX
        # yellow if letter is somehwere else
        elif contains_char(secret, guess[idx]):
            emojis += YELLOW_BOX
        else: #if char isnt present in string at all
            emojis += WHITE_BOX
        idx += 1
    return emojis

def input_guess(expected_len: int) -> str:
    guess: str = input(f"Enter a {expected_len} character word: ")

    # only exit loop once expected length
    while len(guess)!= expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    
    return guess 

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    guessed: bool = False
    user_guess: str = ""

    while (guessed == False and turn < 7):
        print(f"=== Turn {turn}/6 ===")
        user_guess: str = input_guess(len(secret_word))
        # print emojis of secret word to show accuracy
        print(emojified(user_guess, secret_word))
        
        if secret_word == user_guess:
            # this will exit the loop if the guess was correct
            guessed = True
        else:
            turn += 1
    # printing final response once guesses are out or user is correct
    if guessed:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")  

if __name__ == "__main__":
    main()