# Final Project Option: Character Generator Battle Simulator

# Name: Morgan Burke
# Dev 108
# Final project: Character Generator Battle Simulator - Fantasy Edition
# 
# Instructions: 
# Menu System (3 pts)
    # Display all menu options clearly
    # Include an “Exit” option
    # Validate user input for menu choices
# Create a New Character (10 pts)
    # Randomly assign stats such as hit points, strength, defense, etc.
    # Store each character in your CSV file
    # Display stats clearly to the user
# List All Characters (5 pts)
    # Display a neatly formatted table with all characters and their stats
    # Search for a Character (5 pts)
    # Allow users to search by character name
    # Display all relevant stats including wins and losses
# Delete a Character (5 pts)
    # Ask user for a character name to delete
    # Ask for confirmation: “Are you sure?” before deleting
    # Ensure deletion from the CSV file
# Battle System (20 pts)
    # Create an interactive or automated battle between two characters. Your battle system should include:
    # Option to choose characters or pick them randomly
    # Option to control the battle manually (strike, run, heal) or run automatically
    # Turn-based system with random strikes, healing, and hit point deduction
    # Use the time module to pause between actions
    # Display each move clearly for the user to follow
    # Update characters’ stats and record wins/losses in the CSV
    # Allow characters to improve their stats after a win
# Preloaded Characters (3 pts)
    # Include at least 6 characters in your CSV file when submitted so I can test your program easily
# Input Validation (4 pts)
    # Check that user input is valid throughout the program
    # (e.g., numbers for health, acceptable menu choices, etc.)
# User Experience & Formatting (7 pts)
    # Format all output to be readable and user-friendly
    # Use spacing, symbols, and clear messages to guide the player
    # Provide screen feedback that is clear and engaging
# Code Quality & Comments (5 pts)
    # Comment your code clearly (at least one comment per function)
    # Use descriptive names for variables and functions
    # Organize code using a main() function and modular structure
# Test Cases in README (6 pts)
    # Include 3 test cases with sample input and expected output
    # Document how invalid input is handled
# AI Disclosure (2 pts)
    # If you used any AI tools (e.g., ChatGPT, Copilot), include a brief note in your README.md file
    # Explain what you used and how you used it
    # If no AI was used, state that explicitly



import random 
import csv

# create a filename for our .csv file
filename = "characters.csv"

# function to write character names in the CSV file
def write_characters(character):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(character)

# function to read character names in the CSV file
def read_characters():
    characters= []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            characters.append(row)
    return characters

# program title
def title():
    print()
    print("=" * 100)
    print("Welcome to the Character Generator Battle Simulator - Fantasy Edition")
    print("=" * 100)
    print()

# description of program
def description():
    print()
    print("This program is a battle simulator where the user is able to\n"
    "create random fantasy characters to face off with one another\n"
    "to earn the hero title. You have the option to create your own character\n"
    "or the program will create one for you. May the odds be ever in your favor...")
    print()

# display menu of the characters 
def display_menu():
    print()
    print("**********PLAYER MENU**********")
    print("list - List all players")
    print("add -  Add a character")
    print("del -  Delete a character")
    print("find - Find a character by name")
    print("play - Play the program battle")
    print("exit - Exit program")
    print()    

# function to list all characters
def list(character_list):
    if len(character_list) == 0:
        print("There are no characters in the list.\n")
        return
    else:
        i = 1
        for character in character_list:
            row = character
            print(str(i) + ". " + row[0] # list the character name
            + " (" + str(row[1]) + ")" # list the character type
            + " @ " + str(row[2])) # list the character strength

            i += 1
        print()

# function to list character names in the program
def list_characters(characters):
    print("Here is the current list of character options:")
    print()
    print("Character Name\t\tCharacter Type\t\tStrength\t\tIntellect\t\tCharisma\t\tSpeed\t\tHit Points")
    for i in range(0, len(characters)):
        character = characters[i]
        print(str(character[0]) + "\t\t" + str(character[1]) + "\t\t" + str(character[2])+ "\t\t" + str(character[3])+ "\t\t" + str(character[4]) + "\t\t" + str(character[5]) + "\t\t" + str(character[6]))

# function to add a new character to the list
def add(character_list):
    name = input("Character Name: ")
    type = (input("Character Type: "))
    strength = int(input("Strength: "))
    intellect = int(input("Intellect: "))
    charisma = int(input("Charisma: "))
    speed = int(input("Speed: "))
    hit_points = int(input("Hit Points: "))
    character = []
    character.append(name)
    character.append(type)
    character.append(strength)
    character.append(intellect)
    character.append(charisma)
    character.append(speed)
    character.append(hit_points)
    character_list.append(character)
    print(character[0] + " was added.\n")

# function to delete a character
def delete(character_list):
    number = int(input("Number: "))
    if number < 1 or number > len(character_list):
        print("Invalid character number.\n")
    else:
        ask = input("Are you sure you want to delete this character? (y/n) ")
        while True:
            if ask.lower() == "y":
                character = character_list.pop(number-1)
                print(character[0] + " was deleted.\n")
            elif ask.lower() == "n":
                print(character[0] + " was not deleted.\n")
                return display_menu
            else:
                print("Invalid entry.\n")
                return ask

def find_by_name(character_list):
    name = (input("Character Name: "))
    for character in character_list:
        if (character[0]) == name:
            print(character[0] + " is ready to battle if you are.")
            display_character(character[0])
        print()

# ask player name
def get_character_name():
    print("For a character name, you can:\n" \
    "1. Choose a character name from the options in the character list\n" \
    "2. Have the program generate one for you by typing 'random'\n" \
    "3. Create one yourself")
    name = input("Please enter a character name: ").strip()
    # generate a random name if player doesn't enter one in
    while True:
        if name.lower() == "":
            names = ["Shadow", "Blaze", "Ragnar", "Nova", "Ember", "Spirit"] 
        elif name.lower() == "random":
            name = random.choice(names)
        else:
            character = []
            character.append(name)
            character_list.append(character)
        return name

# function to generate random character 
def generate_character_type():
    character_types = ["Human Warrior", "Elf Archer", "Wizard", "Dragon Rider", "Troll Princess", "Mystical Fairy"]
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
    opponent_names = ["Shadow", "Blaze", "Ragnar", "Nova", "Ember", "Spirit"] 
    opponent_name = random.choice(opponent_names) 
    opponent = create_character(opponent_name) 
    print("\nYour opponent has been created!") 
    display_character(opponent) 
    return opponent 


def main():
    title()
    description()

    player_name = input("Before we get started, what is your name? ")

    if player_name == "":
        player_name = "Player"
    print(f"Hello, {player_name}! Welcome to the battleground...")

    characters = read_characters()
    list_characters(characters)

    display_menu()
    while True:
        command = input("Command: ")
        if command == "list":
            list(characters)
        elif command == "add":
            add(characters)
        elif command == "del":
            delete(characters)
        elif command == "find":
            find_by_name(characters)
        elif command == "play":
            play = input(f"{player_name}, would you like to generate a character? (y/n): ")
            while play.lower() == "y":

                # create player character
                name = get_character_name()
                player = create_character(name)
            
                # Display the player's character.
                print("\nYour character has been created!")
                display_character(player)

                # create list for the input of character information
                character = []
                character.append(name)
                character.append()
            
                # Ask whether the player wants to battle
                battle_choice = input(f"\n{player_name}, would you like to battle another character? (y/n): ")
                while battle_choice.lower() == "y":
                    # Create a random opponent.
                    opponent = create_opponent()
            
                    # Run the battle.
                    battle(player, opponent)
            
                    # Ask if the player wants another battle.
                    battle_choice = input(f"\n{player_name}, would you like to battle another character? (y/n): ")
                    print("Darn, no more battles today.")
            
                    # Ask player if they want a completely new character
                    play = input(f"\n{player_name}, would you like to create another character and play again? (y/n): ")
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print(f"\nThank you {player_name} for visting the Random Character Generator - Fantasy Edition!")
    print("Best of luck on your future endeavors.\n" \
    "Just remember, you are a hero to us regardless of your battle outcomes. Bye!!")   
    print()
    
if __name__ == "__main__":
    main()
