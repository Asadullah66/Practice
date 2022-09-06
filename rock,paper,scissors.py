from ast import Continue
import random
options = ["rock","paper","scissors"]
decision = input("Do you wanna play rock , paper , scissors?\n").lower()
if decision != "yes":
    quit()
print("Ok, lets start")

person_pick = input("rock , paper or scissors?\n")
if person_pick not in options:
    Continue
random_number = random.randint(0,2)
computer_pick = options[random_number]
if person_pick == "scissors" and computer_pick == "paper":
    print("Computer picked " + computer_pick + " so you won")
if person_pick == "paper" and computer_pick == "rock":
    print("Computer picked " + computer_pick + " so you won")
if person_pick == "rock" and computer_pick == "paper":
    print("Computer picked " + computer_pick + " so you won")
if person_pick == computer_pick:
    print("Computer also picked " + computer_pick + " so its a tie")
if computer_pick == "paper" and person_pick == "rock":
    print("Computer picked " + computer_pick + " so you lose")
if computer_pick == "rock" and person_pick == "scissors":
    print("Computer picked " + computer_pick + " so you lose")
if computer_pick == "scissors" and person_pick == "rock":
    print("Computer picked " + computer_pick + " so you lose")

while True:
    decision = input("Play again or press Q to quit\n").lower()
    if decision != "yes":
        quit()
    if decision == "q":
        quit()

    person_pick = input("rock , paper or scissors?\n")
    if person_pick not in options:
        Continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    if person_pick == "scissors" and computer_pick == "paper":
        print("Computer picked " + computer_pick + " so you won")
    if person_pick == "paper" and computer_pick == "rock":
        print("Computer picked " + computer_pick + " so you won")
    if person_pick == "rock" and computer_pick == "paper":
        print("Computer picked " + computer_pick + " so you won")
    if person_pick == computer_pick:
        print("Computer also picked " + computer_pick + " so its a tie")
    if  computer_pick == "paper" and person_pick == "rock":
        print("Computer picked " + computer_pick + " so you lose")
    if computer_pick == "rock" and person_pick == "scissors":
        print("Computer picked " + computer_pick + " so you lose")
    if computer_pick == "scissors" and person_pick == "rock":
        print("Computer picked " + computer_pick + " so you lose")


































