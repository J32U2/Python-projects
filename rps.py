import random
from banners import banner

# simple rock paper scissors game,using control flow.

banner("-","ROCK PAPER SCISSORS","*")

choices = ["scissors","rock","paper"]
computer = random.choice(choices)
player = input('choose: ')


print("computer chose: ",computer)

if player == computer:
    print("its a draw!".upper())

elif player == "scissors" and computer == "paper":
    print("scissors cut paper".title())
    print('you win!'.upper())
elif computer == "scissors" and player == "paper":
    print("scissors cut paper".title())
    print("you loose !".upper())

elif player == "rock" and computer == "scissors":
    print("rock smashes scissors".title())
    print("you win !".upper())
elif computer == 'rock' and player == "scissors":
    print("rock smashes scissors".title())
    print("you loose !".upper())

elif player == "paper" and computer == "rock":
    print("paper covers rock !".title())
    print("you win !".upper())
elif computer == "paper" and player == "rock":
    print("paper cover rock !".title())
    print("you loose !".upper())

elif player != "scissors" or "rock" or "paper":(
    print("player, not a valid entry try again.".title()))
