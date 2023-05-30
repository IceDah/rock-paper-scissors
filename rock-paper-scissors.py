import random

rps = ["rock", "paper", "scissors"]

while True:
    user_input = input('rock, paper or scissors? ')
    computer_choice = random.choice(rps)

    while user_input not in rps:
        user_input = input('Please choose one: rock, paper or scissors? ')

    print("You chose = " + str(user_input))
    print("I chose = " + str(computer_choice))

    if user_input == computer_choice:
        print("It's a Tie")
    elif (user_input == "rock" and computer_choice == "scissors") or (user_input == "paper" and computer_choice == "rock") or (user_input == "scissors" and computer_choice == "paper"):
        print("You win")
    else:
        print("You lose")

    restart = input("Restart? y/n ")
    if restart.lower() != "y":
        exit()
