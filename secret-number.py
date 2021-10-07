secret = 4

guess = int(input("Guess the number between 1 and 9: "))

if guess == secret:
    print("Congratulations, you've guessed it!")
else:
    print("Nope, sorry!")
