# The program will be Rock Paper Scissors.

import random
while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()  
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == "rock":
        if computer_choice == "paper":
            print("Computer Wins!")
        elif computer_choice == "rock":
            print("Draw!")
        else:
            print("You won!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("Computer Wins!")
        elif computer_choice == "paper":
            print("Draw!")
        else:
            print("You won!")
    else: #scizzors
        if computer_choice == "paper":
            print("You won!")
        elif computer_choice == "scissors":
            print("Draw!")
        else:
            print("You won!")


    # Your code here
    answer = input("Run again? (y/n): ")
    if answer.lower() != 'y':
        break