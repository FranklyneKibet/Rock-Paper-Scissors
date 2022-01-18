import random


while True:
    player = input("Enter a choice (Rock, Paper, Scissors): ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou choose {player}, computer choose {computer_action}") 

    if player == computer_action: 
        print(f"Both players selected {player}. it's a tie!")
    elif player == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors! You win!")
        else: 
            print("Paper covers Rock! You lose!")
    elif player == "Paper": 
        if computer_action == "Rock": 
            print("Paper covers Rock! You win!")
        else: 
            print("Scissors cuts paper! You lose!")
    elif player == "Scissors":
        if computer_action == "Paper": 
            print("Scissors cut paper, You win!")
        else: 
            print("Rock Smashes Scissors! You loose!")

    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y": 
        break
