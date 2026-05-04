import random

while True:
    numbers = range(0,101)
    chosen = random.choice(numbers)
    # print(chosen)

    for i in range(1, 6):
        print(f"Guess number {i}")
        guess = input("Guess a number from 0-100: ")
        guess = int(guess)

        if guess == chosen:
            print(f"Congrats! The number chosen was {chosen}")
            break
        elif guess < chosen:
            print("Higher")
        else:
            print("Lower")

        if i == 5 and guess != chosen:
            print(f"Sorry! The number chosen was {chosen}")

    again = input("Try again? Y/N: ")
    if again.lower() != "y":
        break
        