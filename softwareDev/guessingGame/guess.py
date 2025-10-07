#generate random number
import random
number = random.randint(1, 10)
#guessing game
def guessing_game():
    print("Welcome to the Guessing Game!")
    guess = None
    count = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number.")
        count += 1
    print(f"You took {count} attempts to guess the number.")
        
if __name__ == "__main__":
    guessing_game()
    