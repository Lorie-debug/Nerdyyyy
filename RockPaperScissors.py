import random
choices = ["rock", "paper", "scissors"]
playing = True

while playing:
    player = None
    computer = random.choice(choices)
    
    while player not in choices:
        player = input("Enter your choices (rock, paper, scissors): ")
        
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper') or (player == 'rock' and computer ==  'paper'):
        print("You win!!!!!")
    # elif player == "paper" and computer == "rock":
    #     print("You win!!")
    # elif player == "scissors" and computer == "paper":
    #     print('You win!')
    # elif player == 'rock' and computer == 'scissors':
    #     print('You win!')
    else:
        print("You lose!!!")
    if not input("Do you want to play (y/n): ").lower() == 'y':
        playing = False
print("Thank you for playing")