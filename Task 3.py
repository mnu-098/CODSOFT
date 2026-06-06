import random

print("Welcome to Rock Paper Scissors!")

while True:
    user = input("Choose Rock, Paper, or Scissors: ").lower()

    options = ["rock", "paper", "scissors"]

    if user not in options:
        print("Please enter a valid choice.")
        continue

    computer = random.choice(options)

    print("\nYou chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose!")

    elif user == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")

    elif user == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
    