# Placeholder for project 3 character generator program

# Morgan Burke
# Code Practice Project 3 Random character generator
# Dev 108 Summer 2026
# 8/3/2026

# Instructions
# Create a character generator program for a Role Playing game using Codespaces project03-character/main.py fileLinks to an external site.. 
# The character can be any type of character you want it to be. 
# You can opt for standard Dungeons and Dragons style here, or go with any other character you might want. 
# I've had people build generators for ice cream sundaes, robots, cars, musicians, parents, Nintendo characters, cartoon characters, superheroes, famous artists, relationship/family predictions, etc. Be creative. Have fun! 
# The program must do the following: 
#       Comment your code with your name, date, assignment title, and class. 
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

# program title
def title():
    print()
    print("=" * 100)
    print("Welcome to the Random Character Generator - Fantasy Edition")
    print("=" * 100)
    print()
    print("This program will create random fantasy characters to face off in battle with other characters to earn the hero title.")

# ask player name
def get_character_name():
    name = input("Please enter your character name: ").strip()
    # generate a random name if player doesn't enter one in
    if name == "":
        names = ["Shadow", "Blaze", "Ragnar", "Nova", "Ember"] 
        name = random.choice(names)
    return name

# function to generate random character 
def generate_character_type():
    character_types = ["Human Warrior", "Elf Archer", "Wizard", "Dragon Rider", "Troll Princess"]
    return random.choice(character_types)

# function create a character and passes the name as a parameter
def create_character(name):
    character = {}

    character["name"] = name
    character["type"] = generate_character_type()

    # generates random stats for characters
    character["strength"] = random.randint(5, 20)
    character["intellect"] = random.randint(5, 20)
    character["charisma"] = random.randint(5, 20)
    character["speed"] = random.randint(5, 20)
    character["hit_points"] = random.randint(30, 60)
    return character


# function displays all character information
def display_character(character):
    print("\n" + "=" * 45) 
    print(" YOUR CHARACTER INFORMATION") 
    print("=" * 45) 
    print(f"Name: {character['name']}") 
    print(f"Type: {character['type']}") 
    print(f"Strength: {character['strength']}") 
    print(f"Intellect: {character['intellect']}") 
    print(f"Charisma: {character['charisma']}") 
    print(f"Speed: {character['speed']}") 
    print(f"Hit Points: {character['hit_points']}") 
    print("=" * 45)
    print()

# battle function between characters
# Characters attack each other until one reaches 0 HP.
# Characters also have a chance to heal during battle.
def battle(character1, character2): 
    print("\n" + "=" * 55) 
    print(" BATTLE ARENA") 
    print("=" * 55)
    print(f"\n{character1['name']} the {character1['type']} " f"vs. {character2['name']} the {character2['type']}!")

# Save the original hit points so the character can be used again. 
    character1["current_hp"] = character1["hit_points"] 
    character2["current_hp"] = character2["hit_points"]

    round_number = 1

# Continue battling until one character reaches 0 HP.
    while character1["current_hp"] > 0 and character2["current_hp"] > 0:
        print(f"\n--- Round {round_number} ---")

        # Character 1 attacks Character 2
        attack1 = random.randint(5, 15) + character1["strength"] // 3 
        character2["current_hp"] -= attack1

        if character2["current_hp"] < 0: 
            character2["current_hp"] = 0
        print(f"{character1['name']} attacks for {attack1} damage!")
        print(f"{character2['name']} has " f"{character2['current_hp']} HP remaining.")

        # Check if Character 2 has been defeated. 
        if character2["current_hp"] <= 0: 
            break

        # Character 2 attacks Character 1. 
        attack2 = random.randint(5, 15) + character2["strength"] // 3 
        character1["current_hp"] -= attack2

        if character1["current_hp"] < 0: 
            character1["current_hp"] = 0 
            print(f"{character2['name']} attacks for {attack2} damage!") 
            print(f"{character1['name']} has " f"{character1['current_hp']} HP remaining.")

        # Random chance for Character 1 to heal. 
        if character1["current_hp"] > 0 and random.randint(1, 5) == 1: 
            healing = random.randint(5, 12) 
            character1["current_hp"] += healing 
            if character1["current_hp"] > character1["hit_points"]:
                character1["current_hp"] = character1["hit_points"] 
                print(f"{character1['name']} magically heals " f"for {healing} HP!")

        # Random chance for Character 2 to heal. 
        if character2["current_hp"] > 0 and random.randint(1, 5) == 1: 
            healing = random.randint(5, 12) 
            character2["current_hp"] += healing 
            if character2["current_hp"] > character2["hit_points"]: 
                character2["current_hp"] = character2["hit_points"] 
                print( f" {character2['name']} magically heals " f"for {healing} HP!" )

        round_number += 1

    # Determine the winner. 
    print("\n" + "=" * 55) 
    print("BATTLE OVER!") 
    print("=" * 55) 
    if character1["current_hp"] > 0: 
        print(f"WINNER: {character1['name']} " f"the {character1['type']}!" ) 
    else: 
        print(f"WINNER: {character2['name']} " f"the {character2['type']}!" )


# Create a random opponent. 
def create_opponent():
    opponent_names = ["Shadow", "Blaze", "Ragnar", "Nova", "Ember"] 
    opponent_name = random.choice(opponent_names) 
    opponent = create_character(opponent_name) 
    print("\nYour opponent has been created!") 
    display_character(opponent) 
    return opponent 


def main():
    title()

    player_name = input("Before we get started, what is your name? ")

    if player_name == "":
        player_name = "Player"
    print(f"Hello, {player_name}!")

    play = input("Would you like to generate a character? (y/n): ")
    while play.lower() == "y":
        # create player character
        name = get_character_name()
        player = create_character(name)

        # Display the player's character.
        print("\nYour character has been created!")
        display_character(player)

        # Ask whether the player wants to battle
        battle_choice = input("\nWould you like to battle another character? (y/n): ")
        while battle_choice.lower() == "y":
            # Create a random opponent.
            opponent = create_opponent()

            # Run the battle.
            battle(player, opponent)

             # Ask if the player wants another battle.
            battle_choice = input("\nWould you like to battle another character? (y/n): ")
        print("Darn, no more battles today.")

        # Ask player if they want a completely new character
        play = input("\nWould you like to create another character and play again? (y/n): ")

    print("\nThanks for playing the Random Character Generator - Fantasy Edition!")
    print("Have a great day! Bye!!")   

    
if __name__ == "__main__":
    main()
