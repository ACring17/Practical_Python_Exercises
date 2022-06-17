import random

n = random.randint(1,100)
guess = int(input("What number am I thinking of between 1 and 100?\n"))

while n != guess:
    if guess < n:
        print("Guess is too low.")
        guess = int(input("What number am I thinking of between 1 and 100?\n"))
    elif guess > n:
        print("Guess is too high.")
        guess = int(input("What number am I thinking of between 1 and 100?\n"))
    else:
        print("You got it!")
        break



