#my first project with Python 
import random

def number_guessing_game():

    # The computer randomly selects a number
    secret_number = random.randint(1, 100)
    attempt_count = 0
    
    print("I have chosen a number between 1 and 100. Try to guess it!")

    # Continue until the user guesses correctly
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempt_count += 1
            
            if guess < secret_number:
                print("Try a larger number!")
            elif guess > secret_number:
                print("Try a smaller number!")
            else:
                print(f"Congratulations! You guessed the number in {attempt_count} attempts!")
                break  # End the game when the correct guess is made
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    number_guessing_game()


 