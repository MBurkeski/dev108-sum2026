# Placeholder for project 3 character generator program

# Morgan Burke
# Code Practice Project 3 Random character generator
# Dev 108 Summer 2026
# 8/3/2026

# Instructions
# Create a character generator program for a Role Playing game using Codespaces project03-character/main.py fileLinks to an external site.. The character can be any type of character you want it to be. You can opt for standard Dungeons and Dragons style here, or go with any other character you might want. 
# I've had people build generators for ice cream sundaes, robots, cars, musicians, parents, Nintendo characters, cartoon characters, superheroes, famous artists, relationship/family predictions, etc. Be creative. Have fun! 
# The program must do the following: 
#       X Comment your code with your name, date, assignment title, and class. 
#       Comment your code to document your code process. 
#       Ask if the user would like to generate a character (or whatever your program will do). 
#       Ask for a character name. Or provide a name for them. 
#       Import and use the random module.
#       Generate at least 5 different characteristics of a character (such as strength, intellect, hit points, wisdom, charisma, etc.) and assign a random value to each of them. 
#       Use at least one list.
#       Use at least TWO functions. One function must pass a parameter. 
#       Use a random number and if statement to generate a class/race or character type (such as human warrior, or alien from Mars, etc.) 
#       Output the character information and all of their stats in a user friendly format. 
#       Ask if the user would like to create a different character. 
# Continue to expand upon your program by adding a BATTLE depending on the type of character you've chosen to create. 
# Create a second character with random stats and build a loop that carries out a battle between the two characters, deducting from the character's hit points and possibly randomly healing a character until someone's hit points fall to 0 or below. 
# Output the battle scene and declare the winner. Ask if the player would like to battle again before ending the program. 
# At the end of the program, be sure to also ask if they would like to generate another set of characters and play again. 

import random 

# title
print("Welcome to the Random Character Generator - Master Baker Edition")
print()
print("In this program you will develop your own character to face off with other bakers to earn the Master Baker title.")

# ask player name
player_name = input("Before we get started, what is your chef name?")
print("Hello, Chef " + {player_name} + "!")

# ask to play the game
play_game = input(f"Chef {player_name} , would you like to play? (y/n) ")
while True:
    if play_game == "y":

    if play_game == "n":

    else:
        print("Sorry, invalid entry. Please try again.")


# ask player if they want to create a new character
again = "y"
while again.lower() == "y":

else:
    print("No worries, goodbye!")
    

