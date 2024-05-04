import random


def get_guess():
    value = input("What is your guess?")
    if value.lower() in ['x', 'n', 's']:
          return value.lower()
    elif value.isdigit() == True:
         return int(value)
    else:
         print("Enter a valid value")


def guessing_game(number): 
    tries = 0
    while True:
        guess = get_guess()
        if type(guess)==int:
            tries += 1
            if guess > number:
                print("To High")
                print("Try again")
            elif guess < number:
                print("To Low")
                print("Try again")
            else:
                print("You're correct!")
                print(f"Number of Tries: {tries}")
                return 'win'
        elif guess == 'n':
            print ("End game")
            return 'n'
        elif guess == 's':
            print(f"Hidden number: {number}")
        elif guess == 'x':
            print("Exit")
            return 'x'
    


def main():
    number = random.randrange(1,20) 
    while True:
        result = guessing_game(number)
        if result == 'x':
            break
        if result == 'win':
            play_again = input("Do you want to play another game? (yes/no)")
            if play_again.lower() != 'yes':
                print("Thanks for playing!")
                break
            else:
                number = random.randrange(1,20)
        elif result == 'n':
            reset = input("Do you want to play a new game? (yes/no)")
            if reset.lower() != 'yes':
                print("Thanks for playing!")
                break
            else:
                number = random.randrange(1,20)