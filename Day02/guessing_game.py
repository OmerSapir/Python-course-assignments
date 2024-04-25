import random


number = random.randrange(1,20)
tries = 0
while True:
    guess = int(input("What is your guess?"))
    tries += 1
    if guess > number:
        print("To High")
        print("Try again")
    elif guess<number:
        print("To Low")
        print("Try again")
    else:
        print("You're correct!")
        print(f"Number of Tries: {tries}")
        break