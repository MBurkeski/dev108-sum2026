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
import time

# create a filename for our .csv file
filename = "characters.csv"

# write all characters in the CSV file
def write_characters(characters):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Character Number",
            "Character Name",
            "Character Type",
            "Strength",
            "Intellect",
            "Charisma",
            "Speed",
            "Hit Points",
            "Wins",
            "Losses"]) 
    # actually puts the info in the rows of the CSV file
        writer.writerows(characters)

# read characters from the CSV file
def read_characters():
    characters = []

    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            # Skip the header row.
            next(reader, None)
            for row in reader:
                # Only accept rows with all 10 required columns.
                if len(row) == 10:
                    characters.append(row)

    except FileNotFoundError:
        pass

    # If there are no valid characters, create six preloaded characters.
    if len(characters) == 0:
        characters = [
            [1, "Shadow", "Human Warrior", 18, 12, 15, 17, 55, 0, 0],
            [2, "Blaze", "Dragon Rider", 20, 10, 14, 16, 60, 0, 0],
            [3, "Ragnar", "Troll Princess", 19, 8, 11, 9, 58, 0, 0],
            [4, "Nova", "Wizard", 10, 20, 18, 13, 45, 0, 0],
            [5, "Ember", "Elf Archer", 15, 17, 16, 20, 50, 0, 0],
            [6, "Spirit", "Mystical Fairy", 8, 19, 20, 18, 40, 0, 0]]

        # Save the six characters to the CSV file.
        write_characters(characters)

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
    print("1. List all characters")
    print("2. Add a character")
    print("3. Delete a character")
    print("4. Find a character")
    print("5. Play a battle")
    print("6. Exit")
    print()    

# function to list all characters
def list_characters(characters):
    if len(characters) == 0:
        print("There are no characters in the list.\n")
        return

    print("\nCurrent Character List:\n")

    print(
        f"{'No.':<5}"
        f"{'NAME':<15}"
        f"{'TYPE':<20}"
        f"{'STRENGTH':<12}"
        f"{'INTELLECT':<12}"
        f"{'CHARISMA':<12}"
        f"{'SPEED':<10}"
        f"{'HIT POINTS':<12}"
        f"{'WINS':<8}"
        f"{'LOSSES':<8}")

    print("-" * 124)

    for character in characters:
        print(
            f"{character[0]:<5}"
            f"{character[1]:<15}"
            f"{character[2]:<20}"
            f"{character[3]:<12}"
            f"{character[4]:<12}"
            f"{character[5]:<12}"
            f"{character[6]:<10}"
            f"{character[7]:<12}"
            f"{character[8]:<8}"
            f"{character[9]:<8}")
    print()      

# Ask for a name, create a random character, and save it to the CSV.
def add_character(characters):
    name = input("Character Name: ").strip()

    # Make sure the user enters a name.
    while name == "":
        print("Character name cannot be blank. Please enter a name.")
        name = input("Character Name: ").strip()

    # Check whether the name is already being used.
    for character in characters:
        if character[1].lower() == name.lower():
            print("That character name is already being used. Please try again.")
            return

    # Create the new character.
    character = create_character(name, characters)

    # Add the character to the list.
    characters.append(character)

    # Save the updated list to the CSV.
    write_characters(characters)

    # Display the new character.
    print("\n" + "=" * 45)
    print("CHARACTER CREATED!")
    print("=" * 45)
    print(f"Name:       {character[1]}")
    print(f"Type:       {character[2]}")
    print(f"Strength:   {character[3]}")
    print(f"Intellect:  {character[4]}")
    print(f"Charisma:   {character[5]}")
    print(f"Speed:      {character[6]}")
    print(f"Hit Points: {character[7]}")
    print(f"Wins:       {character[8]}")
    print(f"Losses:     {character[9]}")
    print("-" * 45)

# function to delete a character
def delete_character(characters):
    name = input("Enter the name of the character you want to delete: ").strip()

    # Check whether the character exists.
    found_character = None

    for character in characters:
        if character[1].lower() == name.lower():
            found_character = character
            break

    # If the character was not found, stop the function.
    if found_character is None:
        print(f"\nNo character named '{name}' was found.")
        return

    # Show the character before deleting.
    print(f"\nYou selected: {found_character[1]}")

    # Ask for confirmation.
    confirmation = input("Are you sure you want to delete this character? (y/n): ").strip().lower()
    if confirmation == "y":
        characters.remove(found_character)

        # Rewrite the CSV so the deleted character is removed from the file.
        write_characters(characters)
        print(f"\n{found_character[1]} was deleted successfully.")

    elif confirmation == "n":
        print(f"\n{found_character[1]} was not deleted.")
        return

    else:
        print("\nInvalid response. Please enter 'y' or 'n'.")
        return 

def find_by_name(characters):
    name = input("Character Name: ").strip()

    found = False

    for character in characters:
        if character[1].lower() == name.lower():
            print("Your character was found:")
            print("-" * 50)
            print(f"Name:       {character[1]}")
            print(f"Type:       {character[2]}")
            print(f"Strength:   {character[3]}")
            print(f"Intellect:  {character[4]}")
            print(f"Charisma:   {character[5]}")
            print(f"Speed:      {character[6]}")
            print(f"Hit Points: {character[7]}")
            print(f"Wins:       {character[8]}")
            print(f"Losses:     {character[9]}")
            print("-" * 50)
            print("Your character is ready to battle if you are.")
            found = True
            break

    if not found:
        print(f"\nNo character named '{name}' was found.\n")
        print()

# function to generate random character type
def generate_character_type():
    character_types = [
        "Human Warrior", 
        "Elf Archer", 
        "Wizard", 
        "Dragon Rider", 
        "Troll Princess", 
        "Mystical Fairy"]
    return random.choice(character_types)

# function create a character and passes the name as a parameter
def create_character(name, characters):
    character_number = 1
    for character in characters:
        if int(character[0]) >= character_number:
            character_number = int(character[0]) + 1
    character_type = generate_character_type()

    strength = random.randint(5, 20)
    intellect = random.randint(5, 20)
    charisma = random.randint(5, 20)
    speed = random.randint(5, 20)
    hit_points = random.randint(30, 60)

    character = [
        character_number,
        name,
        character_type,
        strength,
        intellect,
        charisma,
        speed,
        hit_points,
        0,
        0]

    return character

# user to choose two characters or have the program choose randomly.
def choose_battle_characters(characters):
    if len(characters) < 2:
        print("\nYou need at least two characters to start a battle.")
        return None, None
    
    print("\n" + "=" * 50)
    print("             CHOOSE YOUR BATTLE CHARACTERS")
    print("=" * 50)
    print("For this battle, you can either:")
    print("1. Choose two characters")
    print("2. Choose characters randomly")
    print()

    while True:
        choice = input("Choose an option (1-2): ").strip()
        if choice == "1":
            list_characters(characters)

            while True:
                first_name = input("\nEnter the first character's name: ").strip()
                first_character = None
                for character in characters:
                    if character[1].lower() == first_name.lower():
                        first_character = character
                        break

                if first_character is not None:
                    break
                print("Character not found. Please try again.")
            
            while True:
                second_name = input("Enter the second character's name: ").strip()
                second_character = None

                for character in characters:
                    if character[1].lower() == second_name.lower():
                        second_character = character
                        break
                if second_character is not None and second_character != first_character:
                    break
                if second_character == first_character:
                    print("A character cannot battle themselves.")
                else:
                    print("Character not found. Please try again.")

            return first_character, second_character

        elif choice == "2":
            first_character, second_character = random.sample(characters, 2)
            print("\nThe computer selected:")
            print(f"{first_character[1]} vs. {second_character[1]}!")
            return first_character, second_character

        else:
            print("Invalid choice. Please enter 1 or 2.")

def choose_battle_mode():
    print("\n" + "=" * 50)
    print("              CHOOSE YOUR BATTLE MODE")
    print("=" * 50)
    print("For this battle, you can either:")
    print("1. Manual battle")
    print("2. Automatic battle")
    print()

    while True:
        choice = input("Choose battle mode (1-2): ").strip()
        if choice == "1":
            return "manual"
        elif choice == "2":
            return "automatic"
        else:
            print("Invalid choice. Please enter 1 or 2.")

# battle function between characters
def battle(character1, character2, mode, characters):
    print("\n" + "=" * 100)
    print("                    LET THE BATTLE BEGIN")
    print("=" * 100)

    print(f"\n{character1[1]} the {character1[2]}")
    print("     VS.")
    print(f"{character2[1]} the {character2[2]}")

    print("\nGet ready!")
    time.sleep(2)

    # Store the original hit points.
    max_hp1 = int(character1[7])
    max_hp2 = int(character2[7])

    # Current hit points change during the battle.
    current_hp1 = max_hp1
    current_hp2 = max_hp2

    round_number = 1

    # Continue until one character reaches zero HP.
    while current_hp1 > 0 and current_hp2 > 0:
        print("\n" + "-" * 50)
        print(f"ROUND {round_number}")
        print("-" * 50)

        print(f"{character1[1]}: {current_hp1} HP")
        print(f"{character2[1]}: {current_hp2} HP")

        time.sleep(1)

        # Character 1 takes a turn.
        action = battle_action(character1, mode)

        if action == "run":
            print(f"\n{character1[1]} ran away!")
            print(f"{character2[1]} wins by default!")

            character2[8] = str(int(character2[8]) + 1)
            character1[9] = str(int(character1[9]) + 1)

            improve_character(character2)

            write_characters(characters)

            return character2

        elif action == "heal":
            healing = random.randint(5, 12)
            current_hp1 += healing

            if current_hp1 > max_hp1:
                current_hp1 = max_hp1
            print(f"\n{character1[1]} heals for {healing} HP!")
            print(f"{character1[1]} now has {current_hp1} HP.")

        elif action == "strike":
            damage = random.randint(5, 15) + int(character1[3]) // 3
            current_hp2 -= damage

            if current_hp2 < 0:
                current_hp2 = 0
            print(f"\n{character1[1]} strikes!")
            print(f"{character1[1]} deals {damage} damage!")
            print(f"{character2[1]} has {current_hp2} HP remaining.")

        time.sleep(1)

        # Check whether character 2 has been defeated.
        if current_hp2 <= 0:
            break

        # Character 2 takes a turn.
        action = battle_action(character2, mode)

        if action == "run":
            print(f"\n{character2[1]} ran away!")
            print(f"{character1[1]} wins by default!")

            character1[8] = str(int(character1[8]) + 1)
            character2[9] = str(int(character2[9]) + 1)

            improve_character(character1)

            write_characters(characters)

            return character1

        elif action == "heal":
            healing = random.randint(5, 12)
            current_hp2 += healing

            if current_hp2 > max_hp2:
                current_hp2 = max_hp2

            print(f"\n{character2[1]} heals for {healing} HP!")
            print(f"{character2[1]} now has {current_hp2} HP.")

        elif action == "strike":
            damage = random.randint(5, 15) + int(character2[3]) // 3

            current_hp1 -= damage

            if current_hp1 < 0:
                current_hp1 = 0

            print(f"\n{character2[1]} strikes!")
            print(f"{character2[1]} gives {damage} damage!")
            print(f"{character1[1]} has {current_hp1} HP remaining.")

        time.sleep(1)

        round_number += 1

    # Determine the winner.
    if current_hp1 > 0:
        winner = character1
        loser = character2
    else:
        winner = character2
        loser = character1

    print("\n" + "*" * 100)
    print("                    BATTLE OVER!")
    print("*" * 100)
    print(f"\nWINNER: {winner[1]} the {winner[2]}!")
    print(f"LOSER:  {loser[1]} the {loser[2]}!")

    # Update wins and losses.
    winner[8] = str(int(winner[8]) + 1)
    loser[9] = str(int(loser[9]) + 1)

    # Improve the winner's stats.
    improve_character(winner)

    # Save the updated results to the CSV.
    write_characters(characters)

    return winner

# Choose an action during a manual or automatic battle.
def battle_action(character, mode):

    if mode == "automatic":
        actions = ["strike", "strike", "strike", "heal"]
        return random.choice(actions)

    print(f"\n{character[1]}'s turn!")
    print("1. Strike")
    print("2. Heal")
    print("3. Run")

    while True:
        choice = input("Choose an action (1-3): ").strip()
        if choice == "1":
            return "strike"
        elif choice == "2":
            return "heal"
        elif choice == "3":
            return "run"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Improve one random stat after a character wins a battle.
def improve_character(character):
    stat_choices = [
        ("Strength", 3),
        ("Intellect", 4),
        ("Charisma", 5),
        ("Speed", 6)]
    stat_name, stat_index = random.choice(stat_choices)

    character[stat_index] = str(int(character[stat_index]) + 1)

    print(f"\n⭐ {character[1]} has improved!")
    print(f"{stat_name} increased to {character[stat_index]}!")


def main():
    title()
    description()

    player_name = input("Before we get started, what is your name? ").strip()

    if player_name == "":
        player_name = "Player"

    print(f"\nHello, {player_name}! "
        "Welcome to the battleground!")

    # Load characters from the CSV file.
    characters = read_characters()

    while True:
        display_menu()

        choice = input(
            "Please choose an option (1-6): ").strip()

        # List all characters.
        if choice == "1":
            list_characters(characters)

        # Create a new character.
        elif choice == "2":
            add_character(characters)

        # Delete a character.
        elif choice == "3":
            delete_character(characters)

        # Search for a character.
        elif choice == "4":
            find_by_name(characters)

        # Start a battle.
        elif choice == "5":
            character1, character2 = choose_battle_characters(characters)

            if character1 is not None and character2 is not None:
                mode = choose_battle_mode()
                battle(
                    character1,
                    character2,
                    mode,
                    characters)

        # Exit the program.
        elif choice == "6":
            print(f"\nThank you for playing, {player_name}!")
            print("Best of luck in your future battles!")
            break

        # invalid menu choice
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")
    print()        
    print("Just remember, you are a hero to us regardless of your battle outcomes. Bye!!")   
    print()
    
if __name__ == "__main__":
    main()
