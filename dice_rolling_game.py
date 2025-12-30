import random

while True:
    print("Roll the dice? (y/n): ")
    answer = input().lower()
    if answer == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Die 1: {die1}, Die 2: {die2}")
    elif answer == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input")