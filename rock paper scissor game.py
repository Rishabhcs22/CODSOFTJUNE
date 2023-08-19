import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    player_choice_num = input("Enter your choice (1/2/3/4): ")

    if player_choice_num == '4':
        print("Thanks for playing. Goodbye!")
        break

    if player_choice_num not in ['1', '2', '3']:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        continue

    player_choice = choices[int(player_choice_num) - 1]
    computer_choice = random.choice(choices)

    print("Your choice:", player_choice)
    print("Computer's choice:", computer_choice)

    result = determine_winner(player_choice, computer_choice)
    print(result)
