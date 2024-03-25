import random
import time

def intro():
    name = input("May I ask you for your name?:")
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick(max_guesses):
    number = random.randint(1, 200)
    guesses_taken = 0

    while guesses_taken < max_guesses:
        try:
            guess = int(input("Guess: "))

            if 1 <= guess <= 200:
                guesses_taken += 1
                if guess < number:
                    print("The guess of the number is too low.")
                elif guess > number:
                    print("The guess of the number is too high.")
                else:
                    print("Good job,!You guessed my number in {} guesses!".format(guesses_taken))
                    return
            else:
                print("Silly Goose! Please enter a number between 1 and 200.")

        except ValueError:
            print("I don't think that's a number. Sorry.")

    print("Nope. The number I was thinking of was {}.".format(number))

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    intro()
    pick(6)
    play_again = input("Do you want to play again? (yes/no):")
