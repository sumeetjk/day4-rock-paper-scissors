import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    ai_choice = random.randint(0, 2)

    print("Computer Chose:")

    print(game_images[ai_choice])


    if user_choice == 0 and ai_choice == 2:
        print("you win")
    elif ai_choice == 0 and user_choice == 2:
        print("You lose")
    elif ai_choice > user_choice:
        print("You lose")
    elif user_choice > ai_choice:
        print("You win")
    elif user_choice == ai_choice:
        print("It's a draw")



###################################################################################################

# hand_sign = ["rock", "paper", "scissors"]

# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# user_choice = hand_sign[choice]

# random_index = random.randint(0, len(hand_sign) -1)

# ai_choice = hand_sign[random_index]

# if user_choice == "rock" and ai_choice == "scissors":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("You win")
# elif user_choice == "rock" and ai_choice == "paper":
#     print(rock)
#     print("Computer chose:")
#     print(paper)
#     print("You lose")
# elif user_choice == "rock" and ai_choice == "rock":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("Its a draw")
# elif user_choice == "paper" and ai_choice == "rock":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("Yow win")
# elif user_choice == "paper" and ai_choice == "paper":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("Its a draw")
# elif user_choice == "paper" and ai_choice == "scissors":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("You lose")
# elif user_choice == "scissors" and ai_choice == "paper":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("You win")
# elif user_choice == "scissors" and ai_choice == "scissors":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("Its a draw")
# elif user_choice == "scissors" and ai_choice == "rock":
#     print(rock)
#     print("Computer chose:")
#     print(scissors)
#     print("You Lose")
