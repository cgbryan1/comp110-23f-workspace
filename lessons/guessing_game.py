"""Game that only completes when you guess the right number."""

from random import randint

secret: int = randint(1, 10)
guess: int = int(input("Guess a number between 1 and 10: "))
tries: int = 1

while guess != secret:
    print("wrong!")
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    if guess > secret:
        print("Your guess was too high!")
    else:
        print("Your guess was too low!")
    tries += 1
    guess = int(input("Guess again! "))
print("You got it in " + str(tries) + " tries!")