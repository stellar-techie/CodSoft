#ROCK PAPER SCISSORS GAME

import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(your_choice, computer_choice):
    if your_choice == computer_choice:
        return 'tie'
    elif (your_choice == 'rock' and computer_choice == 'scissors') or \
         (your_choice == 'scissors' and computer_choice == 'paper') or \
         (your_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    your_score = 0
    computer_score = 0
    
    while True:
        print("WELCOME TO THE GAME!")
        your_choice = input("select your choice (rock, paper, or scissors): ").lower()
        if your_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice.")
            continue
        computer_choice = get_computer_choice()
        winner = determine_winner(your_choice, computer_choice)
        
        print(f"You chose: {your_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if winner == 'tie':
            print("heyyyy, It's a tie!")
        elif winner == 'user':
            print("hurrayyy! You win!")
            your_score += 10
        else:
            print("00ps! Computer wins!")
            computer_score += 10
        print(f"your score: {your_score}")
        print(f"Computer's score: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("Thank you for playing! come back again.")
if __name__ == "__main__":
    play_game()
