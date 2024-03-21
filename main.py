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

hand_sign = ["rock", "paper", "scissors"]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

user_choice = hand_sign[choice]

random_index = random.randint(0, len(hand_sign) -1)

ai_choice = hand_sign[random_index]

if user_choice == "rock" and ai_choice == "scissors":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win")
elif user_choice == "rock" and ai_choice == "paper":
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You lose")
elif user_choice == "rock" and ai_choice == "rock":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("Its a draw")
elif user_choice == "paper" and ai_choice == "rock":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("Yow win")
elif user_choice == "paper" and ai_choice == "paper":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("Its a draw")
elif user_choice == "paper" and ai_choice == "scissors":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You lose")
elif user_choice == "scissors" and ai_choice == "paper":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win")
elif user_choice == "scissors" and ai_choice == "scissors":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("Its a draw")
elif user_choice == "scissors" and ai_choice == "rock":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You Lose")
