import random

while True:
    answer = input("Roll the dice? (y/n): ").lower()
    if answer == "y":
        print("How many dice do you want to roll? (1-6): ")
        num_dice = int(input())
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        print(f"You rolled {dice_rolls}")
    elif answer == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input")