# Placeholder for Madlibs main.py file

# Name: Morgan Burke
# Date: 7/26/2026
# Programming Project 2: Mad Libs

# Instructions
# Output a title for the game.
# Ask if the user would like to play a game.
# Ask for the players name. Greet the player.
# Ask the player to choose from TWO story ideas you have created.  Use an if statement here to separate the code for each choice.
# Ask the player to input between 6 to 10 names/words/numbers to fill in spots for your story. 
# Please do not go over 10 inputs because it can get very long to run/test the programs! 
# Create a short story to go along with the gameplay, substituting their inputted words into the story. 
# Each story should be different and ask for different inputs. 
# Do not reuse the same inputs for each story please. Your stories should be at a minimum of 4 sentences. 
# Ask if the user would like to play again (use a loop for this). 
# Validate the user input as being y/n. If they input something that is NOT one of your options, ask the player to try again. 
# Validate the user input for the story selection. 
# If they input something that is NOT one of your options, ask the player to try again. 
# Create a counter to record how many stories they have created. 
# Display the counter before asking if they would like to play again. 

# Mad lib title
print()
print("Welcome to the Nurse Mad Lib Game!")
print()
print("Instructions: \nIn this game, you will be asked to provide words to fill in the blanks of a story.\nYou will have two story options to choose from.\nAfter you have completed your story, you will be asked if you would like to play again.")
print()

# initialize variables
counter = 0

# ask player name and greet player
player_name = input("What is your first name? ")
print("Hello, "+ player_name + "!") 

# set the default for the while loop to run the first time
again = "y"
while again.lower() == "y":
    # ask to play
    print()
    while True: 
        initial_ask = input(f"{player_name}, would you like to play? (y/n) ")
        if initial_ask.lower() == "y":
            print("Yay! Let's get started.") 
            print()

            # player chooses storyline
            print("Here are your story line options: ")
            print("a. Med Surg\nb. Emergency Department ")
            print()
            story_line = input("What story line did you choose? (a or b) ")
            print()
            print("Great! Now let's get some information to build your story!")
            print()
            if story_line.lower() == "a":
                adjective1 = input("Please provide an adjective: ")
                name1 = input("Please provide a name: ")
                adjective2 = input("Please provide an adjective: ")
                number = input("Please provide a number: ")
                plural_noun = input("Please provide a plural noun: ")
                noun = input("Please provide a noun: ")
                verb = input("Please provide a verb (present tense): ")
                counter += 1
                print()
                print(f"{player_name}, here is your story: \n\nThe {adjective1} nurse {name1} was working in the {adjective2} Med Surg unit. They had to take care of {number} patients with {plural_noun}. One patient had a {noun} that needed to be treated, so they had to {verb} quickly to help them. It was a busy day, but {name1} loved their job and helping others.")
                print()
                print(f"Congratulations {player_name}, you have completed your story!")
                print(f"You have created {counter} stories so far!")
                print()

            elif story_line.lower() == "b":
                adjective3 = input("Please provide an adjective: ")
                name2 = input("Please provide a name: ")
                number2 = input("Please provide a number: ")
                adjective4 = input("Please provide an adjective: ")
                noun2 = input("Please provide a noun: ")
                adjective5 = input("Please provide an adjective: ")
                plural_noun2 = input("Please provide a plural noun: ")
                counter += 1
                print()
                print(f"{player_name}, here is your story: \n\nIt was a {adjective3} night at the hospital. Nurse {name2} had just started thier shift when the alarm in Room {number2} went off. They rushed in and found a {adjective4} patient holding a {noun2}. 'Everything's {adjective5}!' the patient exclaimed, pointing at the {plural_noun2} on the floor. Suddenly {name2} realized they had to act fast to save the day!")
                print()
                print(f"Congratulations {player_name}, you have completed your story!")
                print(f"You have created {counter} stories so far!")
                print()
            else:
                print("Invalid entry, story line a or b are the only options. Please try again.")

        elif initial_ask.lower() == "n":
            print("Darn, maybe next time. Bye!")
            break
        else:
            print("Invalid entry please use a 'y' for yes and a 'n' for no to play the Nurse Mad Lib Game.")
            print()
# ask the player if they want to play again
again = input("Would you like to play again? (y/n): ")
while again.lower() == "n":
    print("No worries. Have a nice day! Bye!")  
    break
else:
    print("Invalid entry, please use a 'y' for yes and a 'n' for no to play the Nurse Mad Lib Game again.")
  
