import random

def play_game():
    print("Welcome to the guessing game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess == secret_number:
            print("Congratulations, you guessed the number in", attempts, "attempts!")
            break
        elif guess < secret_number:
            print("Too low, try again!")
        else:
            print("Too high, try again!")

play_game()