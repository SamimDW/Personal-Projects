import random

def guess_the_number():
    print("welcome to guess the number!")
    number_to_guess = random.randint(1,100) # Random number from 1 to 100
    attempts = 0
    max_attempts = 10 # Number of attempts allowed

    print("I am thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:

            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You have guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    if guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

#run the game       
guess_the_number()
