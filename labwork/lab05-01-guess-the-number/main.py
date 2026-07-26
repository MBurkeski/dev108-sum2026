# starting Guess the Number program from our textbook (page 125)

# Morgan Burke
# 7/23/2026
# Code Practice Lab 5: Guess the Number program


# instructions:
# Be sure to use functions as the starting program does. 
# Ask for player's name. Output their name at least once.
# Ask player if they would like to play an EASY, MEDIUM or HARD game.
#       easy = range of 1 to 10, limit tries to 5.
#       medium = range of 1 to 100, limit tries to 8.
#       hard = range of 1 to 1000, limit tries to 10.
# If the player doesn't guess the number in the required amount of tries, they lose the game.
# Keep track of the wins and loses for the player, displaying the score before asking if they would like to play again. 
# Be sure to create a comment at the top of the program with your name, the date, and the class number, and assignment name.
# Include comments to describe what you are doing in your program. Refer to your textbook code examples for an appropriate level of comments. 

import random

print()
def display_title():
    print("Guess the number!")
    print()

def get_name():
    player_name = input("What is your name? ")
    print("Hello, ", player_name, ".")

def play_game(wins):    # play game function
    level = input("What game level would you like to play? E is for easy,\nM is for medium, and H is for hard. ")

    if level.lower() == "e":
        max_number = 10
        tries = 5
    elif level.lower() == "m":
        max_number = 100
        tries = 8
    elif level.lower() == "h":
        max_number = 1000
        tries = 10
    else:
        print("Sorry! Invalid input. Please try again.")

    number = random.randint(1, max_number)
    print(f"I'm thinking of a number from 1 to " + str(max_number) +"\n")
    count = 1

    while count <= tries:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            print(f"You guessed it in " + str(count) + " tries.\n")
            # count for wins total
            wins += 1
            print("You have won ", wins, "game(s).")
            return wins
    else:
        print("Sorry, you ran out of guesses, the number was ", number) 

def main():     # main function
    display_title()
    get_name()
    # initialize variables
    wins = 0
    again = "y"
    while again.lower() == "y":
        wins = play_game(wins)
        again = input("Would you like to play again? (y/n): ")
        print()
    print("No, worries. Have a nice day! Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
