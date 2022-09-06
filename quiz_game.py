from http.client import OK
from xml.dom.minicompat import StringTypes
print("Welcome to a computer quiz")
playing = input("Do you want to play?\n").lower()
if playing != "yes":
    quit()
print("OK, lets play")
score = 0
answer = input("1) What does CPU stands for?\n")
if answer.lower() == "central processing unit":
    print("Your answer is correct :)")
    score += 1
else:
    print("No, that wrong answer :(")

answer = input("2) What does PC stands for?\n")
if answer.lower() == "personal computer":
    print("Your answer is correct :)")
    score += 1
else:
    print("No, that wrong answer :(")

answer = input("3) Whats 7 times 8?\n")
if answer.lower() == "56":
    print("Your answer is correct :)")
    score += 1
else:
    print("No, that wrong answer :(")
answer = input("4) Who is the owner of Tesla?\n")
if answer.lower() == "elon musk":
    print("Your answer is correct :)")
    score += 1
else:
    print("No, that wrong answer :(")

print("You got " + str(score) + " questions correct!")