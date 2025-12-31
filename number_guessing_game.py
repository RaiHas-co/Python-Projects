import random

while True:
    try:
        min = int(input("Enter the minimum number: "))
        max = int(input("Enter the maximum number: "))
        if min < max:
            break
        else:
            print("The minimum number must be less than the maximum number!")
    except ValueError:
        print("Please enter a valid number!")

num = random.randint(min, max)


while True:
    try:
        guess = int(input(f"Guess the number between {min} and {max}: "))
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break
    except ValueError:
        print("Please enter a valid number!")