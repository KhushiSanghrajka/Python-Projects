import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0]
options[1]
options[2]
while True:
    user_input = input("Type any one: Rock/ Paper/ Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Type valid option!")
        continue
    random_number = random.randint(0,2)
    #1 for rock, 2 for paper, 3 for scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick=="scissors":
        print("You won!")
        user_wins += 1
    elif user_input== "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input=="scissors" and computer_pick =="paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Tie!")
        continue    
    else:
        print("You Lost... Better luck next time")
        computer_wins += 1
print("You won ", user_wins, "times.")
print("Computer won ", computer_wins, "times.")      
if user_wins > computer_wins:
    print("You won the match!!")
elif user_wins == computer_wins:
    print("This match was a TIE..")     
else:
    print("The computer wins the match... Sorry")        
print("Goodbye!")
