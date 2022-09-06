import random
top_of_range = input("Type a number: ")
tries = 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a digit")
    quit()
random_number = random.randrange(0, top_of_range)
user_guess = input("Make a guess of number lower than " + str(top_of_range) + " :")
if user_guess.isdigit():
    user_guess = int(user_guess)
else:
    print("Please type a digit")
    quit()
if user_guess == random_number:
    print("You got it!")
    quit()
elif user_guess < random_number:
    print("its higher than " + str(user_guess))
    tries += 1
else:
    print("its lower than " + str(user_guess))   
    tries += 1
while True:
    user_guess = input("Again make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a digit")
        continue
    if user_guess == random_number:
        print("You got it in " + str(tries) + " tries")
        quit()
    elif user_guess < random_number:
        print("its higher than " + str(user_guess))
        tries += 1
    else:
        print("its lower than " + str(user_guess))   
        tries += 1
    