import random

emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}
choices = ('r', 'p', 's')

while True:
    user_choice = input("Rock, Paper, Scissor? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid input, please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose {emojis[user_choice]}, \ncomputer chose {emojis[computer_choice]}.")

    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'n':
        break   