import random

num = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break
    except ValueError:
        print("Please enter a valid number!")